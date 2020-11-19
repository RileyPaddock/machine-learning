import random
import sys
sys.path.append('src')
from deprecated_polynomial_regressor import PolynomialRegressor

def f(x, rand):
        return 3+0.5*x**2+rand

data = [(x/10,f(x/10,random.randint(-5,5))) for x in range(1,101)]

smallest_error = []
for _ in range(10):
    rand = random.randint(-5,5)
    train_error = []
    test_error = []
    for x in range(1,6):
        regressor = PolynomialRegressor(degree = x)
        regressor.ingest_data(data)
        regressor.solve_coefficients()
        train_error.append((regressor.sum_squared_error(),x))
        regressor.data = [(i+0.4, f(i+0.4,rand)) for i in range(10)]+[(j+0.8, f(j+0.8,rand)) for j in range(10)]
        test_error.append((regressor.sum_squared_error(),x))
    print(test_error)
    smallest_error.append(test_error.index(min(test_error))+1)
print(smallest_error)