import sys
sys.path.append('src')
from dataframe import DataFrame
from decision_tree import DecisionTree
df = DataFrame.from_array(
    [[1, 11, 'A'],
    [1, 12, 'A'],
    [2, 11, 'A'],
    [1, 13, 'B'],
    [2, 13, 'B'],
    [3, 13, 'B'],
    [3, 11, 'B']],
    columns = ['x', 'y', 'class']
)
dt = DecisionTree(df)
print("\n Testing root indices")
assert dt.root.row_indices == [0, 1, 2, 3, 4, 5, 6]
print("     passed")

print("\n Testing root class counts")
assert dt.root.class_counts == {'A': 3,'B': 4}
print("     passed")

print("\n Testing root impurity")
assert round(dt.root.impurity,3) == 0.490
print("     passed")

print("\n Testing root possible splits")
rounded = [[x[0],x[1],round(x[2],3)] for x in dt.root.possible_splits.to_array()]
assert rounded ==  [['x', 1.5,  0.085], ['x', 2.5,  0.147],['y', 11.5, 0.085], ['y', 12.5, 0.276]]
print("     passed")

print("\n Testing root best_split")
assert dt.root.best_split == ('y', 12.5)
print("     passed")

print("\n Testing root low indices")
dt.split()
assert dt.root.low.row_indices == [0, 1, 2, 6]
print("     passed")

print("\n Testing root high indices")
assert dt.root.high.row_indices == [3, 4, 5]
print("     passed")

print("\n Testing root low impurity")
assert round(dt.root.low.impurity,3) == 0.375
print("     passed")

print("\n Testing root high impurity")
assert dt.root.high.impurity == 0
print("     passed")

print("\n Testing root low possible splits")
rounded = [[x[0],x[1],round(x[2],3)] for x in dt.root.low.possible_splits.to_array()]
assert rounded == [['x', 1.5,  0.125], ['x', 2.5,  0.375], ['y', 11.5, 0.042]]
print("     passed")

print("\n Testing root low best split")
assert dt.root.low.best_split == ('x', 2.5)
print("     passed")

print("\n Testing root low low indices")
dt.split()
assert dt.root.low.low.row_indices == [0, 1, 2]
print("     passed")

print("\n Testing root low high indices")
assert dt.root.low.high.row_indices == [6]
print("     passed")

print("\n Testing root low low impurity")
assert dt.root.low.low.impurity == 0
print("     passed")

print("\n Testing root low high impurity")
assert dt.root.low.high.impurity == 0
print("     passed")