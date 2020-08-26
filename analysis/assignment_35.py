import math
import sys
sys.path.append('src')
from matrix import Matrix


data = [[1, 0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  1],
        [1, 0,  0,  1,  0,    0,  0,  0,  0,  0,  0,  1],
        [1, 0,  0,  0,  1,    0,  0,  0,  0,  0,  0,  4],
        [1, 0,  0,  1,  1,    0,  0,  0,  0,  0,  1,  0.1],
        [1, 5,  0,  0,  0,    0,  0,  0,  0,  0,  0,  4],
        [1, 5,  0,  1,  0,    0,  5,  0,  0,  0,  0,  8],
        [1, 5,  0,  0,  1,    0,  0,  5,  0,  0,  0,  1],
        [1, 5,  0,  1,  1,    0,  5,  5,  0,  0,  1,  0.1],
        [1, 0,  5,  0,  0,    0,  0,  0,  0,  0,  0,  5],
        [1, 0,  5,  1,  0,    0,  0,  0,  5,  0,  0,  0.1],
        [1, 0,  5,  0,  1,    0,  0,  0,  0,  5,  0,  9],
        [1, 0,  5,  1,  1,    0,  0,  0,  5,  5,  1,  0.1],
        [1, 5,  5,  0,  0, 25,  0,  0,  0,  0,  0,  0.1],
        [1, 5,  5,  1,  0, 25,  5,  0,  5,  0,  0,  0.1],
        [1, 5,  5,  0,  1, 25,  0,  5,  0,  5,  0,  0.1],
        [1, 5,  5,  1,  1, 25,  5,  5,  5,  5,  1,  0.1]]

def f(x):
    return math.log((10/x)-1)

def regress(data):
    Inputs = []
    Results = []
    for i in range(len(data.elements)):
        Inputs.append([])
        for j in range(len(data.elements[i])-1):
            Inputs[i].append(data.elements[i][j])
    Inputs = Matrix(Inputs)
    for i in range(len(data.elements)):
        Results.append([f(data.elements[i][len(data.elements[i])-1])])
    Results = Matrix(Results)
    x_tpose = Inputs.transpose()
    data = (((x_tpose @ Inputs).inverse() @ x_tpose) @ Results).elements
    result = []
    for elem in data:
        result.append(elem[0])
    return result

def fill_in_interaction_terms(coords):
    iterations = len(coords)
    new_coords = coords
    for i in range(iterations):
        for j in range(iterations):
            if j > i:
                new_coords.append(coords[i] * coords[j])
    new_coords.insert(0,1)
    return new_coords


def evaluate(data, coords):
    correct_coords = fill_in_interaction_terms(coords)
    exponent = 0
    for i in range(len(correct_coords)):
        exponent += coords[i]*data[i]
    return 10/(1+math.exp(1)**exponent)
    #

data_2 = regress(Matrix(data))

print("Testing: no ingredients: ")
assert round(evaluate(data_2,[0,0,0,0]),2) ==  2.66, 'Failed No ingredients'
print("passed")
print("Testing: mayo only: ")
assert round(evaluate(data_2,[0,0,1,0]),2) == 0.59, 'Failed mayo only'
print("passed")
print("Testing: mayo and jelly: ")
assert round(evaluate(data_2, [0,0,1,1]),2) == 0.07, 'Failed mayo and jelly'
print("passed")
print("5 slices beef + mayo: ")
assert round(evaluate(data_2, [5,0,1,0]),2) == 7.64, 'Failed 5 slices beef and mayo'
print("passed")
print("Testing: 5 tbsp pb + jelly: ")
assert round(evaluate(data_2,[0,5,0,1]),2) == 8.94, 'Failed 5 tbsp pb and jelly'
print('passed')
print("Testing: 5 slices beef + 5 slices pb + mayo + jelly: ")
assert round(evaluate(data_2,[5,5,1,1]),2) == 0.02, 'Failed All toppings'
print('passed')