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

def __main__():
    data = [[2,13,'B'],[2,13,'B'],[2,13,'B'],[2,13,'B'],[2,13,'B'],[2,13,'B'],
        [3,13,'B'],[3,13,'B'],[3,13,'B'],[3,13,'B'],[3,13,'B'],[3,13,'B'],
        [2,12,'B'],[2,12,'B'],
        [3,12,'A'],[3,12,'A'],
        [3,11,'A'],[3,11,'A'],
        [3,11.5,'A'],[3,11.5,'A'],
        [4,11,'A'],[4,11,'A'],
        [4,11.5,'A'],[4,11.5,'A'],
        [2,10.5,'A'],[2,10.5,'A'],
        [3,10.5,'B'],
        [4,10.5,'A']]

    df = DataFrame.from_array(data, columns = ['x', 'y', 'class'])
    df = df.append_columns({'node_index':[i for i in range(len(df.to_array()))]})

    r = RandomTree(10)
    r.fit(df)
    print(r.predict())