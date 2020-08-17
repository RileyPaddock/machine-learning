import math
import sys
sys.path.append('src')
from matrix import Matrix

class Logistic_Regressor:
    def __init__(self,data):
        self.data = data

    def solve_coefficients(self):
        X = Matrix([[1,x] for x,y in self.data])
        Y = Matrix([[math.log((1/y) - 1)] for x,y in self.data])
        x_tpose = X.transpose()
        return ((x_tpose @ X).inverse() @ (x_tpose @ Y)).elements

    def evaluate(self,coefficients, time):
        return 1/(1 + (math.exp(1)**(coefficients[0][0] + (coefficients[1][0]*time))))

    def reverse_evaluate(self,coefficients,skill):
        return (math.log((1/skill) - 1) - coefficients[0][0])/coefficients[1][0]


