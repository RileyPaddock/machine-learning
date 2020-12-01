from node import Node
from dataframe import DataFrame
class DecisionTree:
    def __init__(self,df):
        self.df = df.append_columns({'node_index':[i for i in range(len(df.to_array()))]})
        self.root = Node(self.df)
        
    def lowest_level(self,level):
        if level.impurity != 0 and level.low == None and level.high == None:
            return level
        else:
            if level.low.impurity != 0 and level.low.low == None and level.low.high == None:
                return self.lowest_level(level.low)
            elif level.high.impurity != 0 and level.high.low == None and level.high.high == None:
                return self.lowest_level(level.high)
        

    def split(self):
        lowest_level = self.lowest_level(self.root)
        split = lowest_level.best_split
        greater = [entry for entry in lowest_level.df.to_array() if entry[ord(split[0])-120] >= split[1]]
        less = [entry for entry in lowest_level.df.to_array() if entry[ord(split[0])-120] < split[1]]
        lowest_level.high = Node(DataFrame.from_array(greater,['x','y','class','node_index']))
        lowest_level.low = Node(DataFrame.from_array(less,['x','y','class','node_index']))
