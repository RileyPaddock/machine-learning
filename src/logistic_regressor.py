from linear_regressor import LinearRegressor
from dataframe import DataFrame
import math
class LogisticRegressor(LinearRegressor):
    def __init__(self,data_class, prediction_column, max_value,zero_rep = 0.01, max_rep = 0.99,constant = True):
        super().__init__(data_class, prediction_column)
        self.max_value = max_value
        self.original_data = DataFrame.from_array(data_class.to_array(),data_class.columns)
        self.original_data = self.original_data.append_columns({'constant':[1 for _ in range(len(data_class.to_array()))]},['constant']+data_class.columns)
        self.data = data_class.apply(self.prediction_column, lambda x: self.set_bound_replacements(zero_rep,max_rep,x))
        if constant:
            self.data = self.data.append_columns({'constant':[1 for _ in range(len(self.data.to_array()))]},['constant']+self.data.columns)
        self.multipliers = self.solve_coefficients()

    def predict(self, input_set, coefficients = None):
        if coefficients == None:
            coefficients = self.multipliers
        inputs = self.gather_all_inputs(input_set)
        result = self.max_value/(1+(math.exp(sum([input_set[key]*coefficients[key] for key in input_set]))))
        return result
        
    def set_bound_replacements(self,zero_rep, max_rep,x):
        if x == 0:
            return math.log((self.max_value/(zero_rep)) - 1)
        elif x == self.max_value:
            return math.log((self.max_value/(max_rep)) - 1)
        else:
            print(x)
            return math.log((self.max_value/(x)) - 1)

    def calc_rss(self,coefficients):
        #you transform the y component then find the distance
        error = []
        for coord in self.original_data.to_array():
            guess = self.predict({self.data.columns[i]:coord[i] for i in range(len(self.multipliers))},coefficients)
            # print(coord)
            # print({self.data.columns[i]:coord[i] for i in range(len(self.multipliers))})
            # print(self.multipliers)
            # print(guess)
            # print((coord[-1]-guess)**2)
            # print('\n')
            error.append(coord[-1]-guess)

        #print( sum([x**2 for x in error]))
        return sum([x**2 for x in error])

    def set_coefficients(self,coefficients):
        self.multipliers = coefficients

    def get_point_gradient(self,delta):
        gradient = {key:0 for key in self.multipliers}
        for key in self.multipliers:
            forward = dict(self.multipliers)
            forward[key] = self.multipliers[key]+delta
            backward = dict(self.multipliers)
            backward[key] = self.multipliers[key]-delta
            gradient[key] = (self.calc_rss(forward) - self.calc_rss(backward)) / (2 * delta)
        return gradient
    
    def calc_gradient(self,alpha, delta, num_steps, debug_mode = False):
        for _ in range(num_steps):
            gradient = self.get_point_gradient(delta)
            coefficients = {key:self.multipliers[key] for key in self.multipliers}
            for key in self.multipliers:
                self.multipliers[key] = coefficients[key] - (alpha * gradient[key])
            if debug_mode:
                print('step '+str(_))
                print('\tgradient: '+str(gradient))
                print('\tcoeffs: '+str(self.multipliers))
                print('\trss: '+str(self.calc_rss(self.multipliers)))
                
                print('\n')

            





