import sys
sys.path.append('src')
from logistic_regressor import LogisticRegressor
from dataframe import DataFrame

data_dict = {
    'beef': [0, 0, 0, 0, 5, 5, 5, 5, 0, 0, 0, 0, 5, 5, 5, 5],
    'pb': [0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 5, 5, 5],
    'condiments': [[],['mayo'],['jelly'],['mayo','jelly'],
                   [],['mayo'],['jelly'],['mayo','jelly'],
                   [],['mayo'],['jelly'],['mayo','jelly'],
                   [],['mayo'],['jelly'],['mayo','jelly']],
    'rating': [1, 1, 4, 0, 4, 8, 1, 0, 5, 0, 9, 0, 0, 0, 0, 0]
}
df = DataFrame(data_dict, column_order = ['beef', 'pb', 'condiments'])

df = df.create_dummy_variables()
df = df.append_pairwise_interactions()
df = df.append_columns({
    'constant': [1 for _ in range(len(data_dict['beef']))],
    'rating': [1, 1, 4, 0, 4, 8, 1, 0, 5, 0, 9, 0, 0, 0, 0, 0]
})
df = df.apply('rating', lambda x: 0.1 if x==0 else x)
regressor = LogisticRegressor(df, prediction_column = 'rating', max_value = 10)

print("\n Testing multipliers")
assert regressor.multipliers == {
    'beef': -0.03900793,
    'pb': -0.02047944,
    'mayo': 1.74825378,
    'jelly': -0.39777219,
    'beef_pb': 0.14970983,
    'beef_mayo': -0.74854916,
    'beef_jelly': 0.46821312,
    'pb_mayo': 0.32958369,
    'pb_jelly': -0.5288267,
    'mayo_jelly': 2.64413352,
    'constant': 1.01248436
}, 'Incorrect multipliers'
print("     passed")
 

print("\n Testing prediction #1")
assert regressor.predict({
    'beef': 5,
    'pb': 5,
    'mayo': 1,
    'jelly': 1,
}) == 0.023417480134512895, "Incorrect prediction #1"
print("     passed")
 
print("\n Testing prediction #2")
assert regressor.predict({
    'beef': 0,
    'pb': 3,
    'mayo': 0,
    'jelly': 1,
}) == 7.375370219261697, "Incorrect prediction #2"
print("     passed")
 
print("\n Testing prediction #3")
assert regressor.predict({
    'beef': 1,
    'pb': 1,
    'mayo': 1,
    'jelly': 0,
}) == 0.8076522042721185, "Incorrect prediction #3"
print("     passed")
 
print("\n Testing prediction #4")
assert regressor.predict({
    'beef': 6,
    'pb': 0,
    'mayo': 1,
    'jelly': 0,
}) == 8.770303908281422, "Incorrect prediction #4"
print("     passed")
 