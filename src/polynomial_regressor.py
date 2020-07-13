import sys
sys.path.append('src')
from matrix import Matrix
class PolynomialRegressor:
    def __init__(self,degree):
        self.degree = degree
        self.coefficients = [0 for _ in range(self.degree + 1)]
        self.data = []

    def evaluate(self, x):
        return sum([self.coefficients[i]*x**i for i in range(self.degree+1)])

    def ingest_data(self,data):
        self.data = data

    def sum_squared_error(self):
        #Same code as in GradientDescent just shortened
        return sum([(self.evaluate(x) - y)**2 for (x,y) in self.data])

    def solve_coefficients(self):
        solve = Matrix(shape = (1,1))
        for i in range(len(self.coefficients)):
            self.coefficients[i] = solve.calc_linear_approximation_coefficients(self.data, self.degree)[i][0]

    # def plot(self):
    #     if self.degree == 2:
    #         title = 'y = {} + {}x + {}x^2'.format(round(self.coefficients[0],2), round(self.coefficients[1],2),round(self.coefficients[2],2))
    #         plot_approximation(self.evaluate, self.coefficients[0], self.coefficients[0], self.coefficients[0], self.data, title=title)
