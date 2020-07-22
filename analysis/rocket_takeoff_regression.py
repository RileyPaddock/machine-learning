import sys
sys.path.append('src')
from polynomial_regressor import PolynomialRegressor

data = [(1, 3.1), (2, 10.17), (3, 20.93), (4, 38.71), (5, 60.91), (6, 98.87), (7, 113.92), (8, 146.95), (9, 190.09), (10, 232.65)]

constant_regressor = PolynomialRegressor(degree=2)
constant_regressor.ingest_data(data)
constant_regressor.solve_coefficients()
print("Degree 2:")
print("\n   Coefficients:")
print("\n       "+str(constant_regressor.coefficients[0]))
print("\n       "+str(constant_regressor.coefficients[1])+"x")
print("\n       "+str(constant_regressor.coefficients[2])+"x^2")
print("\n   Evaluation at 200:")
print("\n       "+str(constant_regressor.evaluate(200)))
print("\n   Sum Squared Error:")
print("\n       "+str(constant_regressor.sum_squared_error()))
#coefficients = [-3.1618333333335613, 2.648098484848333, 2.083825757575738]
#approx @ 200: 83879.48816666586

constant_regressor = PolynomialRegressor(degree=3)
constant_regressor.ingest_data(data)
constant_regressor.solve_coefficients()
print("Degree 3:")
print("\n   Coefficients:")
print("\n       "+str(constant_regressor.coefficients[0]))
print("\n       "+str(constant_regressor.coefficients[1])+"x")
print("\n       "+str(constant_regressor.coefficients[2])+"x^2")
print("\n       "+str(constant_regressor.coefficients[3])+"x^3")
print("\n   Evaluation at 200:")
print("\n       "+str(constant_regressor.evaluate(200)))
print("\n   Sum Squared Error:")
print("\n       "+str(constant_regressor.sum_squared_error()))
#coefficients = [-1.9033333333354676, 1.531876456878308, 2.32584498834467, -0.014667832167845063]
#-24004.385850931372
#Even though the cubic has a smaller error than the quadratic the quaadratic is a better approximation because it does not have a turning point like the cubic


