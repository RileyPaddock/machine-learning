import sys
sys.path.append('src')
from dataframe import DataFrame
from decision_tree import DecisionTree

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
print("Testing splits using gini impurity")
dt = DecisionTree('gini', 4)
dt.fit(df)
# print("\n Testing splits")
# assert dt.root.best_split == ('y', 12.5)
# assert dt.root.low.best_split == ('x', 2.5)
# assert dt.root.low.low.best_split == ('y', 11.25)
# assert dt.root.low.high.best_split == ('y', 11)
# assert dt.root.low.high.low.best_split == ('x', 3.5)
# print("     passed")

# print("\n Testing classify")
# assert dt.classify({'x': 2, 'y': 11.5}) == 'B'
# assert dt.classify({'x': 2.5, 'y': 13}) == 'B'
# assert dt.classify({'x': 4, 'y': 12}) == 'A'
# assert dt.classify({'x': 3.25, 'y': 10.5}) == 'B'
# assert dt.classify({'x': 3.75, 'y': 10.5}) == 'A'
# print("     passed")

# print("Testing random splits")
# dt = DecisionTree('random')
# dt.fit(df)

# df = DataFrame.from_array(
#     [[1, 11, 'A'],
#     [1, 12, 'A'],
#     [2, 11, 'A'],
#     [1, 13, 'B'],
#     [2, 13, 'B'],
#     [3, 13, 'B'],
#     [3, 11, 'B']],
#     columns = ['x', 'y', 'class']
# )
# dt = DecisionTree(df)

# dt.root.row_indices
# [0, 1, 2, 3, 4, 5, 6] # these are the indices of data points in the root node

# dt.root.class_counts
# {
#     'A': 3,
#     'B': 4
# }

# dt.root.impurity
# 0.490 # rounded to 3 decimal places

# dt.root.possible_splits.to_array()
# # dt.possible_splits is a dataframe with columns
# # ['feature', 'value', 'goodness of split']
# # Note: below is rounded to 3 decimal places

# [['x', 1.5,  0.085],
#  ['x', 2.5,  0.147],
#  ['y', 11.5, 0.085],
#  ['y', 12.5, 0.276]]

# dt.root.best_split
# print("     passed")

# print("\n Testing root best_split")
# assert dt.root.best_split == ('y', 12.5)
# print("     passed")

# print("\n Testing root low indices")
# dt.split()
# assert dt.root.low.row_indices == [0, 1, 2, 6]
# print("     passed")

# print("\n Testing root high indices")
# assert dt.root.high.row_indices == [3, 4, 5]
# print("     passed")

# print("\n Testing root low impurity")
# assert round(dt.root.low.impurity,3) == 0.375
# print("     passed")

# print("\n Testing root high impurity")
# assert dt.root.high.impurity == 0
# print("     passed")

# print("\n Testing root low possible splits")
# rounded = [[x[0],x[1],round(x[2],3)] for x in dt.root.low.possible_splits.to_array()]
# assert rounded == [['x', 1.5,  0.125], ['x', 2.5,  0.375], ['y', 11.5, 0.042]]
# print("     passed")

# print("\n Testing root low best split")
# assert dt.root.low.best_split == ('x', 2.5)
# print("     passed")

# print("\n Testing root low low indices")
# dt.split()
# assert dt.root.low.low.row_indices == [0, 1, 2]
# print("     passed")

# print("\n Testing root low high indices")
# assert dt.root.low.high.row_indices == [6]
# print("     passed")

# dt = DecisionTree(df)

# print("\n Testing fit")
# dt.fit()

# assert dt.root.high.row_indices == [3, 4, 5]
# assert dt.root.low.low.row_indices == [0, 1, 2]
# assert dt.root.low.high.row_indices == [6]
# print("     passed")