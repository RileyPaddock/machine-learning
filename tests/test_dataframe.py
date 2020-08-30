import sys
sys.path.append('src')
from dataframe import DataFrame
data_dict = {
    'Pete': [1, 0, 1, 0],
    'John': [2, 1, 0, 2],
    'Sara': [3, 1, 4, 0]
}

df1 = DataFrame(data_dict, column_order = ['Pete', 'John', 'Sara'])
print("\n Testing dictionary Input")
assert df1.data_dict == {'Pete': [1, 0, 1, 0], 'John': [2, 1, 0, 2],'Sara': [3, 1, 4, 0]}, 'incorrect dictionary implementation for df1'
print("     passed")

print('\n Testing to_array()')
assert df1.to_array() == [[1, 2, 3], [0, 1, 1], [1, 0, 4], [0, 2, 0]], 'incorrect array for df1'
print("     passed")

print('\n Testing columns')
assert df1.columns == ['Pete', 'John', 'Sara'], 'incorrect columns for df1'
print("     passed")


df2 = df1.filter_columns(['Sara', 'Pete'])
print('\n Testing filter_columns() pt1')
assert df2.to_array() == [[3, 1], [1, 0], [4, 1], [0, 0]], 'incorrect array for df2'
print("     passed")


print('\n Testing filter_columns() pt2')
assert df2.columns == ['Sara', 'Pete'], 'incorrect columns for df2'
print("     passed")


def multiply_by_4(x):
    return 4*x
df3 = df1.apply('John', multiply_by_4)
print('\n Testing apply()')
assert df3.to_array() == [[1, 8, 3], [0, 4, 1], [1, 0, 4], [0, 8, 0]], 'incorrect apply method'
print("     passed")

