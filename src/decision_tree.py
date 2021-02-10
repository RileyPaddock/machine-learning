import random
from dataframe import DataFrame
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


class Node:
    def __init__(self,df, split_metric, depth, goodness_check = False, visited = False):
        self.df = df
        self.split_metric = split_metric
        self.depth = depth
        self.num_vars = len(self.df.to_array()[0])-2
        self.node_split = None
        self.low = None
        self.high = None
        self.row_indices = self.df.data_dict['node_index']
        self.class_counts = self.calc_class_counts()
        self.impurity = self.calc_impurity()
        if not(goodness_check) and self.impurity != 0:
            self.possible_splits = self.possible_splits()
            self.best_split = self.calc_best_split()

    def calc_class_counts(self):
        class_count = {x[len(x)-2]:0 for x in self.df.to_array()}
        for x in self.df.to_array():
            class_count[x[len(x)-2]]+=1
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
            if entry[split[0]] > split[1]:
                greater.append(entry)
            else:
                less.append(entry)
        splits = [Node(DataFrame.from_array(greater,self.df.columns),self.split_metric,self.depth, True),Node(DataFrame.from_array(less,self.df.columns),self.split_metric,self.depth, True)]
        for split in splits:
            to_be_summed.append((len(split.row_indices)/len(self.row_indices)) * split.impurity)
        # 0.5 - 
        return self.impurity - sum(to_be_summed)

    def possible_splits(self):
        possible_splits = []
        features = [self.df.columns[i] for i in range(len(self.df.to_array()[0])-2)]
        distinct = [[] for _ in range(self.num_vars)]
        for i in range(self.num_vars):
            for entry in self.df.to_array():
                if entry[i] not in distinct[i]:
                    distinct[i].append(entry[i])
        for i in range(self.num_vars):
            for j in range(len(distinct[i])-1):
                possible_splits.append((i,(distinct[i][j]+distinct[i][j+1])/2))
        return DataFrame.from_array([[features[entry[0]],entry[1],self.goodness_of_split(entry)] for entry in possible_splits],['axis','point','goodness of split'])
    
    def calc_best_split(self, possible_splits = 'all'):
        if possible_splits == 'all':
            goodness = [x[2] for x in self.possible_splits.to_array()]
        else:
            goodness = [x[2] for x in possible_splits]

        if len(goodness) == 0:
            self.impurity = 0
            majority = max([(self.class_counts[i],i) for i in self.class_counts])
            self.class_counts = {majority[1]:majority[0]}
        else:
            max_goodness_index = goodness.index(max(goodness))
            if possible_splits == 'all':
                return (self.possible_splits.to_array()[max_goodness_index][0],self.possible_splits.to_array()[max_goodness_index][1])
            else:
                return (possible_splits[max_goodness_index][0],possible_splits[max_goodness_index][1])
    def split(self, max_depth):
        if self.depth < max_depth:
            if self.low is None and self.impurity != 0: 
                    if self.split_metric == 'gini':
                        split = self.best_split
                    elif self.split_metric == 'random':
                        random_feature = random.choice(list(set([i for i,j,k in self.possible_splits.to_array()])))
                        split = self.calc_best_split(possible_splits = [entry for entry in self.possible_splits.to_array() if entry[0] == random_feature])
                    self.node_split = split
                    self.low = Node(self.df.select_rows_where(
                        lambda x: x[split[0]] <= split[1]), self.split_metric, self.depth+1)
                    self.high = Node(self.df.select_rows_where(
                        lambda x: x[split[0]] > split[1]), self.split_metric, self.depth+1)
                    return True
            elif self.impurity == 0:
                    return False
            else:
                return self.low.split(max_depth) or self.high.split(max_depth)
        else:
            class_counts = [(self.class_counts[key], key) for key in self.class_counts]
            class_count_nums = [count for count,class_ in class_counts]
            if len(class_counts) == 1 or class_count_nums.count(max(class_count_nums)) == 1:
                self.class_counts = {max(class_counts)[1]:max(class_counts)[0]}
            else:
                rand_choice = random.choice(class_counts)
                self.class_counts = {rand_choice[1]:rand_choice[0]}
            self.impurity = 0
            return False

        