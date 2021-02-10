import random
from dataframe import DataFrame
from decision_tree_node import Node
class DecisionTree:
    def __init__(self, split_metric, max_depth = 9999):
        self.split_metric = split_metric
        self.max_depth = max_depth
        self.features = None
        self.root = None

    def fit(self, df):
        df = df.append_columns({'node_index':[i for i in range(len(df.to_array()))]})
        self.root = Node(df, self.split_metric, 0)
        self.features = [df.columns[i] for i in range(len(df.to_array()[0])-2)]
        while self.root.split(self.max_depth):
            pass

    def classify(self, point, level = None):
        level = self.root if level is None else level
        point_list = [point[k] for k in point]
        if level.impurity == 0:
            for key in level.class_counts:
                return key 
        elif point_list[self.features.index(level.node_split[0])] > level.node_split[1]:
            return self.classify(point,level.high)
        elif point_list[self.features.index(level.node_split[0])] <= level.node_split[1]:
            return self.classify(point,level.low)




        