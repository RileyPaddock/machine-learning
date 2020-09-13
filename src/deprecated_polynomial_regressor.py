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

    def derivative(self,x):
        tangent_line = PolynomialRegressor(1)
        tangent_line.data = [(x - 0.001, self.evaluate(x-0.001)),(x + 0.001, self.evaluate(x+0.001))]
        tangent_line.solve_coefficients()
        return tangent_line.coefficients[1]
    
    def make_data_critical_points(self):
        min = self.data[0]
        max = self.data[0]
        for x,y in self.data:
            if y < min[1]:
                min = (x,y)
            elif y > max[1]:
                max = (x,y)
        self.data.append((max[0] - 0.01, max[1]-0.01))
        self.data.append((max[0] + 0.01, max[1]-0.01))
        self.data.append((min[0] - 0.01, min[1]+0.1))
        self.data.append((min[0] + 0.01, min[1]+0.1))
        self.data.remove(min)
        self.data.remove(max)


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
m = Matrix([[-1,1,-1,1,-2],[1,1,1,1,0],[8,4,2,1,3],[27,9,3,1,4]])
m.show()
m.rref().show()