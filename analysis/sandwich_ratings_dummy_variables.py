# Slices Beef | Tbsp Peanut Butter | Condiments  | Rating |
# --------------------------------------------------------------
#  0          | 0                  | -           |    1   |
#  0          | 0                  | mayo        |    1   |
#  0          | 0                  | jelly       |    4   |
#  0          | 0                  | mayo, jelly |    0   |
#  5          | 0                  | -           |    4   |
#  5          | 0                  | mayo        |    8   |
#  5          | 0                  | jelly       |    1   |
#  5          | 0                  | mayo, jelly |    0   |
#  0          | 5                  | -           |    5   |
#  0          | 5                  | mayo        |    0   |
#  0          | 5                  | jelly       |    9   |
#  0          | 5                  | mayo, jelly |    0   |
#  5          | 5                  | -           |    0   |
#  5          | 5                  | mayo        |    0   |
#  5          | 5                  | jelly       |    0   |
#  5          | 5                  | mayo, jelly |    0   |

import sys
sys.path.append('src')
from matrix import Matrix

def apply_interactoin_terms(data,results):
    matrix = data
    data1 = []
    data2 = []
    for x in range(1,len(matrix.elements[0])+1):
        for y in range(2,len(matrix.elements[0])+1):
            if y > x:
                data1.append(x-1)
                data2.append(y-1)
    for i in range(len(matrix.elements)):
        for j in range(6):
            matrix.elements[i].append(matrix.elements[i][data1[j]] * matrix.elements[i][data2[j]])

    for i in range(len(matrix.elements)):
        matrix.elements[i].append(results.elements[i][0])
    
    return matrix

                    



def regress(data):
    Inputs = []
    Results = []
    for i in range(len(data.elements)):
        Inputs.append([])
        for j in range(len(data.elements[i])-1):
            Inputs[i].append(data.elements[i][j])
    Inputs = Matrix(Inputs)
    for i in range(len(data.elements)):
        Results.append([data.elements[i][len(data.elements[i])-1]])
    Results = Matrix(Results)

    for i in range(len(Inputs.elements)):
        Inputs.elements[i].insert(0,1)
    x_tpose = Inputs.transpose()
    data = ((x_tpose @ Inputs).inverse() @ (x_tpose @ Results)).elements
    result = []
    for elem in data:
        result.append(elem[0])
    return result

def evaluate(data, coords):
    result = data[0]
    for i in range(len(coords)):
        result += data[i+1]*coords[i]
    i = 5
    for x in range(len(coords)):
        for y in range(1,len(coords)):
            if y > x:
                result += coords[x] * coords[y] * data[i]
                i+=1
    return result

    
        
sandwich_data  = Matrix(elements = [[ 0, 0, 0, 0],
 [0, 0, 1, 0],
 [0, 0, 0, 1],
 [0, 0, 1, 1],
 [5, 0, 0, 0],
 [5, 0, 1, 0],
 [5, 0, 0, 1],
 [5, 0, 1, 1],
 [0, 5, 0, 0],
 [0, 5, 1, 0],
 [0, 5, 0, 1],
 [0, 5, 1, 1],
 [5, 5, 0, 0],
 [5, 5, 1, 0],
 [5, 5, 0, 1],
 [5, 5, 1, 1]])
sandwich_results = Matrix(elements = [[1], [1], [4], [0], [4], [8], [1], [0], [5], [0], [9], [0], [0], [0], [0], [0]])

sandwich_data_with_interaction = apply_interactoin_terms(sandwich_data,sandwich_results)
sandwich_data_with_interaction.show()
test = 0
print("\n Testing Sum of Matrix Entries")
for row in sandwich_data_with_interaction.elements:
    for entry in row:
        if entry != 0:
            test += entry
assert test == 313,'Sum of Matrix Entries is not 313'
print("\n Passed")
beta = regress(sandwich_data_with_interaction)

# 2 slices beef + mayo: __
# 2 slices beef + jelly: __
# 3 tbsp peanut butter + jelly: __
# 3 tbsp peanut butter + jelly + mayo: ___
# 2 slices beef + 3 tbsp peanut butter + jelly + mayo: ___


print("\nCOEFFICIENTS")

print("\n   bias term: "+str(beta[0]))

print("\n   beef: "+str(beta[1]))
print("\n   peanut butter: "+str(beta[2]))
print("\n   mayo: "+str(beta[3]))
print("\n   jelly: "+str(beta[4]))

print("\n   beef & peanut butter: "+str(beta[5]))
print("\n   beef & mayo: "+str(beta[6]))
print("\n   beef & jelly: "+str(beta[7]))
print("\n   peanut butter & mayo: "+str(beta[8]))
print("\n   peanut butter & jelly: "+str(beta[9]))
print("\n   mayo & jelly: "+str(beta[10]))

print("\nRatings of certain sandwiches:")
print("\n   2 slices beef + mayo: "+str(evaluate(beta,[2,0,1,0])))
print("\n   2 slices beef + jelly: "+str(evaluate(beta,[2,0,0,1])))
print("\n   3 tbsp peanut butter + jelly: "+str(evaluate(beta,[0,3,0,1])))
print("\n   3 tbsp peanut butter + jelly + mayo: "+str(evaluate(beta,[0,3,1,1])))
print("\n   2 slices beef + 3 tbsp peanut butter + jelly + mayo: "+str(evaluate(beta,[2,3,1,1])))