import random
from node import Node
from dataframe import DataFrame
class DecisionTree:
    def __init__(self, split_metric):
        self.split_metric = split_metric
        self.root = None
        
    def lowest_level(self,level):
        if level.impurity != 0 and level.low == None and level.high == None:
            return level
        else:
            if level.low.impurity != 0 and level.high.impurity != 0:
                if level.low.high == None or (level.low.high.impurity != 0 or level.low.low.impurity !=0):
                    return self.lowest_level(level.low)
                elif level.high.high == None or (level.high.high.impurity != 0 or level.high.low.impurity !=0):
                    return self.lowest_level(level.high)
            elif level.high.impurity != 0:
                return self.lowest_level(level.high)
            elif level.low.impurity != 0:
                return self.lowest_level(level.low)

        

    def split(self):
        lowest_level = self.lowest_level(self.root)
        if lowest_level == None:
            return 'Done'
        if self.split_metric =='gini':
            split = lowest_level.best_split
        elif self.split_metric == 'random':
            split = random.choice([(i,j) for i,j,k in lowest_level.possible_splits.to_array()])
        greater = [entry for entry in lowest_level.df.to_array() if entry[ord(split[0])-120] >= split[1]]
        less = [entry for entry in lowest_level.df.to_array() if entry[ord(split[0])-120] < split[1]]
        lowest_level.high = Node(DataFrame.from_array(greater,['x','y','class','node_index']))
        lowest_level.low = Node(DataFrame.from_array(less,['x','y','class','node_index']))

    def fit(self, df):
        self.root = Node(df)
        while self.split() == None:
            self.split()

    def classify(self, point, level = None):
        level = self.root if level is None else level
        point_list = [point[k] for k in point]
        if level.impurity == 0:
            for key in level.class_counts:
                return key 
        elif point_list[ord(level.best_split[0])-120] >= level.best_split[1]:
            return self.classify(point,level.high)
        elif point_list[ord(level.best_split[0])-120] < level.best_split[1]:
            return self.classify(point,level.low)

        