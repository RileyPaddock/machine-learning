from linear_regressor import LinearRegressor
import math
class LogisticRegressor(LinearRegressor):
    def __init__(self,data_class, prediction_column, max_value):
        super().__init__(data_class, prediction_column)
        self.max_value = max_value
        self.data.data_dict[self.prediction_column] = [math.log((max_value/result) - 1) for result in self.data.data_dict[self.prediction_column]]
        self.multipliers = self.solve_coefficients()

    def predict(self, input_set):
        inputs = self.gather_all_inputs(input_set)
        result = self.max_value/(1+(math.exp(sum([inputs[key]*self.multipliers[key] for key in inputs]))))
        return result
        





