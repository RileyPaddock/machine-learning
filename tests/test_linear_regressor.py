import sys
sys.path.append('src')
from dataframe import DataFrame
from linear_regressor import LinearRegressor

data_dict = {
    'beef': [0, 0, 0, 0, 5, 5, 5, 5, 0, 0, 0, 0, 5, 5, 5, 5],
    'pb': [0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 5, 5, 5],
    'condiments': [[],['mayo'],['jelly'],['mayo','jelly'],
                   [],['mayo'],['jelly'],['mayo','jelly'],
                   [],['mayo'],['jelly'],['mayo','jelly'],
                   [],['mayo'],['jelly'],['mayo','jelly']],
}
df = DataFrame(data_dict)
print("\n Testing columns of DataFrame")
assert df.columns == ['beef', 'pb', 'condiments'],'Incorrect columns for DataFrame'
print("     passed")

df = df.create_dummy_variables()
df = df.append_pairwise_interactions()
df = df.append_columns({
    'constant': [1 for _ in range(len(data_dict['beef']))],
    'rating': [1, 1, 4, 0, 4, 8, 1, 0, 5, 0, 9, 0, 0, 0, 0, 0]
})
print("\n Testing Columns of DataFrame with interaction terms")
assert df.columns == ['beef', 'pb', 'mayo', 'jelly','beef_pb', 'beef_mayo', 'beef_jelly', 'pb_mayo', 'pb_jelly', 'mayo_jelly', 'constant', 'rating'],'Incorrect columns for DataFrame'
print("     passed")

linear_regressor = LinearRegressor(df, prediction_column = 'rating')
print("\n Testing Coefficients of LinearRegressor")
assert linear_regressor.coefficients == {'beef': 0.25, 'pb': 0.4, 'mayo': -1.25, 'jelly': 1.5, 'beef_pb': -0.21, 'beef_mayo': 1.05, 'beef_jelly': -0.85, 'pb_mayo': -0.65, 'pb_jelly': 0.65, 'mayo_jelly': -3.25, 'constant': 2.19}, 'Incorrect coefficients for Linear Regressor'
print("     passed")

print("\n Testing Gathering all inputs of LinearRegressor")
assert linear_regressor.gather_all_inputs({ 'beef': 5, 'pb': 5, 'mayo': 1, 'jelly': 1}) == {'beef': 5, 'pb': 5, 'mayo': 1, 'jelly': 1, 'beef_pb': 25, 'beef_mayo': 5, 'beef_jelly': 5, 'pb_mayo': 5, 'pb_jelly': 5, 'mayo_jelly': 1, 'constant': 1}, 'Incorrect gather_all_inputs'
print("     passed")


print("\n Testing Prediction #1")
assert linear_regressor.predict({'beef': 5, 'pb': 5, 'mayo': 1, 'jelly': 1}) == -1.81, 'Incorrect prediction from linear regressor'
print("     passed")
print("\n Testing Prediction #2")
assert linear_regressor.predict({
    'beef': 0,
    'pb': 3,
    'mayo': 0,
    'jelly': 1,
}) == 6.84 , 'Incorrect prediction from linear regressor'
print("     passed")
print("\n Testing Prediction #3")
assert linear_regressor.predict({
    'beef': 1,
    'pb': 1,
    'mayo': 1,
    'jelly': 0,
}) == 1.78 , 'Incorrect prediction from linear regressor'
print("     passed")
print("\n Testing Prediction #4")
assert linear_regressor.predict({
    'beef': 6,
    'pb': 0,
    'mayo': 1,
    'jelly': 0,
}) == 8.74, 'Incorrect prediction from linear regressor'
print("     passed")