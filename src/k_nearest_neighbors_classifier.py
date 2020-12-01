from dataframe import DataFrame
class KNearestNeighborsClassifier:
    def __init__(self, k):
        self.k = k
        self.data = None
        self.prediction_column = None

    def compute_distances(self, observation):
        distances = []
        for i in range(len(self.data.to_array())):
            distances.append([(sum([(observation[entry] - self.data.data_dict[entry][i])**2 for entry in observation]))**(0.5), self.data.to_array()[i][0]])
        return DataFrame.from_array(distances, columns = ['distance', 'Cookie Type'])

    def nearest_neighbors(self, observation):
        return DataFrame.from_array(sorted(self.compute_distances(observation).to_array()), columns = ['distance', 'Cookie Type']) 

    def compute_average_distances(self, observation):
        sorted_neighbors = self.nearest_neighbors(observation).to_array()
        averages = {}
        for entry in sorted_neighbors:
            averages[entry[1]] = (0,0)
        for entry in sorted_neighbors:
            averages[entry[1]] = (averages[entry[1]][0]+entry[0], averages[entry[1]][1]+1)
        for entry in averages:
            averages[entry] = averages[entry][0]/averages[entry][1]
        return averages

    def fit(self,df,dependant_variable):
        self.data = df
        self.prediction_column = dependant_variable

    def classify(self, observation):
        top_k = [self.nearest_neighbors(observation).to_array()[i] for i in range(self.k)]
        count = {}
        for distance,classification in top_k:
            count[classification] = 0
        for distance,classification in top_k:
            count[classification] += 1
        maxes = sorted([(count[i],i) for i in count])
        if len(maxes)>1 and maxes[0][0] == maxes[1][0]:
            return [i for i in self.compute_average_distances(observation)][0]
        else:
            return maxes[0][1]
