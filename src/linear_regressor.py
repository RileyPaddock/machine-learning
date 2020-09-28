from matrix import Matrix
from dataframe import DataFrame
class LinearRegressor:
    def __init__(self,data_class, prediction_column):
        self.data = data_class
        self.prediction_column = prediction_column
        self.coefficients = self.solve_coefficients()

    def solve_coefficients(self):
        result = {}
        Inputs = Matrix(self.data.remove_columns([self.prediction_column]).to_array())
        Results = Matrix(self.data.remove_columns([key for key in self.data.data_dict if key != self.prediction_column]).to_array())
        x_tpose = Inputs.transpose()
        coefficients = ((x_tpose @ Inputs).inverse() @ (x_tpose @ Results)).elements
        i = 0
        for key in self.data.remove_columns([self.prediction_column]).data_dict:
            result[key] = round(coefficients[i][0], 8)
            i+=1
        return result

    def gather_all_inputs(self,input_set):
        result = {}
        for key in input_set:
            result[key] = input_set[key]
        for key1 in input_set:
            for key2 in input_set:
                if key1 != key2 and (key1 + "_" + key2) not in result and (key2 + "_" + key1) not in result:
                    result[key1 + "_" + key2] = input_set[key1]*input_set[key2]
        result['constant'] = 1
        return result

    
    def predict(self, input_set):
        inputs = self.gather_all_inputs(input_set)
        result = sum([inputs[key]*self.coefficients[key] for key in inputs])
        return result

# data_dict = {
#     'beef': [0, 0, 0, 0, 5, 5, 5, 5, 0, 0, 0, 0, 5, 5, 5, 5],
#     'pb': [0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 5, 5, 5],
#     'condiments': [[],['mayo'],['jelly'],['mayo','jelly'],
#                    [],['mayo'],['jelly'],['mayo','jelly'],
#                    [],['mayo'],['jelly'],['mayo','jelly'],
#                    [],['mayo'],['jelly'],['mayo','jelly']],
# }
# df = DataFrame(data_dict)
# df = df.create_dummy_variables()
# df = df.append_pairwise_interactions()
# df = df.append_columns({
#     'constant': [1 for _ in range(len(data_dict['beef']))],
#     'rating': [1, 1, 4, 0, 4, 8, 1, 0, 5, 0, 9, 0, 0, 0, 0, 0]
# })
# linear_regressor = LinearRegressor(df, prediction_column = 'rating')
# print(linear_regressor.gather_all_inputs({ 'beef': 5, 'pb': 5, 'mayo': 1, 'jelly': 1}))

