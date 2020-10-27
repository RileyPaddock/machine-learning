from dataframe import DataFrame
class KNearestNeighborsClassifier:
    def __init__(self, dataframe, prediction_column):
        self.data = dataframe
        self.prediction_column = prediction_column

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

    def classify(self, observation, k):
        top_k = [self.nearest_neighbors(observation).to_array()[i][1] for i in range(k)]
        return max(set(top_k), key = top_k.count) 