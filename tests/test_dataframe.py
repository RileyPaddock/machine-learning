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

data_dict = {
    'Pete': [1, 0, 1, 0],
    'John': [2, 1, 0, 2],
    'Sara': [3, 1, 4, 0]
}

df1 = DataFrame(data_dict, column_order = ['Pete', 'John', 'Sara'])

print("\n Testing append_pairwise_interactions() pt 1")
df4 = df1.append_pairwise_interactions()
assert df4.columns == ['Pete', 'John', 'Sara', 'Pete_John', 'Pete_Sara', 'John_Sara'], "Incorrect Columns from pairwise_interactions"
print("     passed")

print("\n Testing append_pairwise_interactions() pt 2")
assert df4.to_array() == [[1, 2, 3, 2, 3, 6], [0, 1, 1, 0, 0, 1], [1, 0, 4, 0, 4, 0], [0, 2, 0, 0, 0, 0]], "Incorrect Array for pairwise_interactions"
print("     passed")

data_dict = {
    'id': [1, 2, 3, 4],
    'color': ['blue', 'yellow', 'green', 'yellow']
}

df1 = DataFrame(data_dict, column_order = ['id', 'color'])
df2 = df1.create_dummy_variables()
print("\n Testing create_dummy_variables() pt1")
assert df2.columns == ['id', 'color_blue', 'color_yellow', 'color_green'], 'Incorrect Columns for create_dummy_variables()'
print("     passed")

print("\n Testing create_dummy_variables() pt2")
assert df2.to_array() == [[1, 1, 0, 0], [2, 0, 1, 0], [3, 0, 0, 1], [4, 0, 1, 0]], 'Incorrect Array for create_dummy_variables()'
print("     passed")

df3 = df2.remove_columns(['id', 'color_yellow'])
print("\n Testing remove_columns() pt1")
assert df3.columns == ['color_blue', 'color_green'], 'Incorrect Columns for remove_columns'
print("     passed")

print("\n Testing remove_columns() pt2")
assert df3.to_array() == [[1, 0],[0, 0],[0, 1],[0, 0]], 'Incorrect Array for remove_columns()'
print("     passed")

df4 = df3.append_columns({
    'name': ['Anna', 'Bill', 'Cayden', 'Daphnie'],
    'letter': ['a', 'b', 'c', 'd']
})
print("\n Testing append_columns() pt1")
assert df4.columns == ['color_blue', 'color_green', 'name', 'letter'], 'Incorrect Columns for append_columns'
print("     passed")

print("\n Testing append_columns() pt2")
assert df4.to_array() == [[1, 0, 'Anna', 'a'], [0, 0, 'Bill', 'b'], [0, 1, 'Cayden', 'c'], [0, 0, 'Daphnie', 'd']], 'Incorrect Array for append_columns()'
print("     passed")