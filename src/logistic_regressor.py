from linear_regressor import LinearRegressor
import math
class LogisticRegressor(LinearRegressor):
    def __init__(self,data_class, prediction_column, max_value):
        super().__init__(data_class, prediction_column)
        self.max_value = max_value
        self.data = data_class.apply(self.prediction_column, lambda x: math.log((max_value/(x+0.001)) - 1) if x == 0 else math.log((max_value/(x-0.001)) - 1))
        self.multipliers = self.solve_coefficients()

    def predict(self, input_set):
        inputs = self.gather_all_inputs(input_set)
        result = self.max_value/(1+(math.exp(sum([input_set[key]*self.multipliers[key] for key in input_set]))))
        return result
        





