from matrix import Matrix
from dataframe import DataFrame
import numpy as np 
class LinearRegressor:
    def __init__(self,data_class, prediction_column):
        self.data = data_class
        #self.data = data_class.append_columns({'constant': [1 for _ in range(len(data_class.to_array()))]})
        self.prediction_column = prediction_column
        self.coefficients = self.solve_coefficients()

    def solve_coefficients(self):
        result = {}
        Inputs = Matrix(self.data.remove_columns([self.prediction_column]).to_array())
        Results = Matrix(self.data.filter_columns([self.prediction_column]).to_array())

        x_tpose = Inputs.transpose()

        coefficients = ((x_tpose @ Inputs).inverse() @ (x_tpose @ Results)).elements
        i = 0
        for key in self.data.remove_columns([self.prediction_column]).data_dict:
            result[key] = coefficients[i][0]
            i+=1
        return result

    def gather_all_inputs(self,input_set):
        result = {}
        if len(input_set)+2< len(self.data.columns):
            for key in input_set:
                result[key] = input_set[key]
            for key1 in input_set:
                for key2 in input_set:
                    if key1 != key2 and (key1 + "_" + key2) not in result and (key2 + "_" + key1) not in result:
                        result[key1 + "_" + key2] = input_set[key1]*input_set[key2]
            result['constant'] = 1
        elif len(input_set)+2 == len(self.data.columns):
            result = {column:self.coefficients[column]*input_set[column] for column in input_set}
            result['constant'] = 1
        return result

    
    def predict(self, input_set):
        result = sum([input_set[key]*self.coefficients[key] for key in input_set])
        return result



