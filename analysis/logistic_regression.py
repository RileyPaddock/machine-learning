import math
import sys
sys.path.append('src')
from matrix import Matrix

def solve_coefficients(data):
    X = Matrix([[1,x] for x,y in data])
    Y = Matrix([[math.log((1/y) - 1)] for x,y in data])
    x_tpose = X.transpose()
    return ((x_tpose @ X).inverse() @ (x_tpose @ Y)).elements

data = [(10, 0.05), (100, 0.35), (1000, 0.95)]

def evaluate(coefficients, time):
    return 1/(1 + (math.exp(1)**(coefficients[0][0] + (coefficients[1][0]*time))))

def reverse_evaluate(coefficients,skill):
    return (math.log((1/skill) - 1) - coefficients[0][0])/coefficients[1][0]

print("probability of beating a player with 500 hours:")
decimal = evaluate(solve_coefficients(data),500)
percentage = "{:.0%}".format(decimal)
print("\n   "+str(percentage))
print("skill level of average player: ")
print("\n   "+str(reverse_evaluate(solve_coefficients(data),0.5)))
