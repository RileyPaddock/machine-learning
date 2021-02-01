from dataframe import DataFrame
from decision_tree import DecisionTree
class RandomTree:
    def __init__(self, num_trees):
        self.nt = num_trees
        self.trees = [DecisionTree('random') for _ in range(num_trees)]

    def fit(self, df):
        for tree in self.trees:
            tree.fit(df)
    
    def predict(self, observation):
        votes = []
        for tree in self.trees:
            votes.append(tree.classify(observation))
        d = {i:votes.count(i) for i in votes}
        return sorted([(d[k],k) for k in d])[0][1]

