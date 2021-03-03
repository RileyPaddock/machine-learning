from dataframe import DataFrame


class KNearestNeighborsClassifier:
    def __init__(self, k):
        self.k = k

    def fit(self, df, dependent_variable):
        self.df = df
        self.critical_points = {column: (min(self.df.data_dict[column])+0.01, max(self.df.data_dict[column])) for column in self.df.columns}
        self.dependent_variable = dependent_variable

    def compute_distances(self, observation):
        rows = self.df.remove_columns([self.dependent_variable]).to_array()
        types = self.df.get_column(self.dependent_variable)
        c = [x for x in self.df.columns if x != self.dependent_variable]
        obs = [observation[col] for col in c]
        #print([[ x for x in zip(obs, rows[i], self.df.columns)] for i in range(len(rows))])
        return DataFrame({'distances': [sum(abs(self.f(x,z)-self.f(y,z)) for x, y,z in zip(obs, rows[i], self.df.columns)) for i in range(len(rows))], 'types': types}, ['distances', 'types'])

    def nearest_neighbors(self, observation):
        return self.compute_distances(observation).order_by('distances', ascending=True)

    def f(self,x,col):
        return (x - self.critical_points[col][0])/(self.critical_points[col][1] - self.critical_points[col][0])


    def compute_average_distances(self, obs, k=None):
        k = len(self.df.get_column(self.dependent_variable)) if k is None else k
        distances = self.compute_distances(obs).select_rows(range(k))
        types = distances.get_column('types')
        indices = {t: [i for i in range(
            len(types)) if types[i] == t] for t in set(types)}
        distances = distances.get_column('distances')
        avgs = {t: sum(distances[i] for i in indices[t])/len(indices[t])
                for t in set(types)}
        return avgs

    def classify(self, obs):
        near = self.nearest_neighbors(obs).select_rows(
            range(self.k)).get_column("types")
        type_counts = {t: near.count(t) for t in set(near)}
        m = max(type_counts, key=type_counts.get)
        if list(type_counts.values()).count(type_counts[m]) > 1:
            avgs = self.compute_average_distances(obs, self.k)
            #print(avgs,min(avgs, key = avgs.get))
            return min(avgs, key=avgs.get)
        else:
            return m



