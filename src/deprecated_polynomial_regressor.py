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
        X = Matrix(shape=(len(self.data), 1))
        Y = Matrix(shape=(len(self.data), 1))
        for i, (x, y) in enumerate(self.data):
            X.elements[i] = [x**i for i in range(self.degree + 1)]
            Y.elements[i] = [y]
        x_tpose = X.transpose()
        solve =  ((x_tpose @ X).inverse() @ (x_tpose @ Y))
        for i in range(len(self.coefficients)):
            self.coefficients[i] = solve.elements[i][0]

    def derivative(self,x):
        tangent_line = PolynomialRegressor(1)
        tangent_line.data = [(x - 0.001, self.evaluate(x-0.001)),(x + 0.001, self.evaluate(x+0.001))]
        tangent_line.solve_coefficients()
        return tangent_line.coefficients[1]





# p = PolynomialRegressor(3)
# p.data = [(-1,-2), (1, 0), (2, 3),(3,4)]
# p.make_data_critical_points()
# print(p.data)
# p.solve_coefficients()
# best_error = p.sum_squared_error()
# best_fit = p.coefficients
# for x in range(3,len(p.data)):
#     p = PolynomialRegressor(x)
#     p.data = [(-1,-2),(1,0),(2,3),(3,4)]
#     p.make_data_critical_points()
#     p.solve_coefficients()
#     if p.sum_squared_error() < best_error:
#         best_error = p.sum_squared_error()
#         best_fit = p.coefficients
# print(best_fit)
# m = Matrix([[-1,1,-1,1,-1,1],[1,1,1,1,1,1],[32,16,8,4,2,1],[243,81,27,9,3,1],[5,-4,3,-2,1,0],[405,108,27,6,1,0]])
# n = Matrix([[-2],[0],[3],[4],[0],[0]])
# m.show()
# x_tpose = m.transpose()
# print(((x_tpose @ m).inverse() @ (x_tpose @ n)).elements)