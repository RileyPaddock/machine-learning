import random
import math
from dataframe import DataFrame
from decision_tree import DecisionTree
class RandomForest:
    def __init__(self, num_trees, max_depth = 999, training_percentage = 1):
        self.nt = num_trees
        self.trees = [DecisionTree('random',max_depth) for _ in range(num_trees)]
        self.training_percentage = training_percentage

    def fit(self, df):
        for tree in self.trees:
            print(self.trees.index(tree))
            reduced_data = self.percentage_of_data(df)
            tree.fit(reduced_data)

    def percentage_of_data(self, df):
        size_of_data = len(df.to_array())
        reduced_size = math.floor(size_of_data*self.training_percentage)
        reduced_data = []
        for x in range(reduced_size):
            rand = random.randint(0,size_of_data-1)
            reduced_data.append(df.to_array()[rand])
        return DataFrame.from_array(reduced_data,df.columns)



    def predict(self, observation):
        classifications = []
        for tree in self.trees:
            prediction = tree.classify(observation)
            classifications.append(prediction)
        counted = self.count_predictons(classifications)
        return self.return_max(counted)

    def count_predictons(self, predictions):
        counted = {}
        for prediction in set(predictions):
            counted[prediction] = predictions.count(prediction)
        return counted

    def return_max(self, counted):
        keys = list(counted.keys())
        counts = list(counted.values())
        return keys[counts.index(max(counts))]

