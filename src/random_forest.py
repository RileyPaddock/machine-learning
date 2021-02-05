from dataframe import DataFrame
from decision_tree import DecisionTree
class RandomForest:
    def __init__(self, num_trees):
        self.nt = num_trees
        self.trees = [DecisionTree('random') for _ in range(num_trees)]

    def fit(self, df):
        for tree in self.trees:
            tree.fit(df)
    
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

