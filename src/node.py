from dataframe import DataFrame
class Node:
    def __init__(self,df,goodness_check = False):
        self.df = df
        self.low = None
        self.high = None
        self.row_indices = self.df.data_dict['node_index']
        self.class_counts = self.calc_class_counts()
        self.impurity = self.calc_impurity()
        if self.impurity != 0:
            self.possible_splits = self.possible_splits()
            self.best_split = self.best_split()

    def calc_class_counts(self):
        class_count = {x[2]:0 for x in self.df.to_array()}
        for x in self.df.to_array():
            class_count[x[2]]+=1
        return class_count
    
    def calc_impurity(self):
        individual_impurities = []
        for class_type in self.class_counts:
            class_impurity = self.class_counts[class_type]/len(self.row_indices) * (1 - self.class_counts[class_type]/len(self.row_indices))
            individual_impurities.append(class_impurity)
        return sum(individual_impurities)

    def goodness_of_split(self,split):
        to_be_summed = []
        greater = []
        less = []
        for entry in self.df.to_array():
            if entry[split[0]] >= split[1]:
                greater.append(entry)
            else:
                less.append(entry)
        splits = [Node(DataFrame.from_array(greater,['x','y','class','node_index']),True),Node(DataFrame.from_array(less,['x','y','class','node_index']),True)]
        for split in splits:
            to_be_summed.append((len(split.row_indices)/len(self.row_indices)) * split.impurity)
        return self.impurity - sum(to_be_summed)

    def possible_splits(self):
        possible_splits = []
        distinct = [[],[]]
        for i in range(2):
            for entry in self.df.to_array():
                if entry[i] not in distinct[i]:
                    distinct[i].append(entry[i])
        for i in range(2):
            for j in range(len(distinct[i])-1):
                possible_splits.append((i,(distinct[i][j]+distinct[i][j+1])/2))
        return DataFrame.from_array([[chr(120+entry[0]),entry[1],self.goodness_of_split(entry)] for entry in possible_splits],['axis','point','goodness of split'])
    
    def best_split(self):
        goodness = [x[2] for x in self.possible_splits.to_array()]
        max_goodness_index = goodness.index(max(goodness))
        return (self.possible_splits.to_array()[max_goodness_index][0],self.possible_splits.to_array()[max_goodness_index][1])

