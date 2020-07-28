import sys
sys.path.append('src')
from matrix import Matrix
from polynomial_regressor import PolynomialRegressor
#   1 * beta_0 + 0 * beta_1 + 0 * beta_2 = 1
#   1 * beta_0 + 1 * beta_1 + 0 * beta_2 = 2
#   1 * beta_0 + 2 * beta_1 + 0 * beta_2 = 4
#   1 * beta_0 + 4 * beta_1 + 0 * beta_2 = 8
#   1 * beta_0 + 6 * beta_1 + 0 * beta_2 = 9
#   1 * beta_0 + 0 * beta_1 + 2 * beta_2 = 2
#   1 * beta_0 + 0 * beta_1 + 4 * beta_2 = 5
#   1 * beta_0 + 0 * beta_1 + 6 * beta_2 = 7
#   1 * beta_0 + 0 * beta_1 + 8 * beta_2 = 6

#   [[1, 0, 0],                   [[1],
#    [1, 1, 0],                    [2],
#    [1, 2, 0],                    [4],
#    [1, 4, 0],    [[beta_0],      [8],
#    [1, 6, 0],     [beta_1],  =   [9],     
#    [1, 0, 2],     [beta_2]]      [2],
#    [1, 0, 4],                    [5],
#    [1, 0, 6],                    [7],
#    [1, 0, 8]]                    [6]]

#rating = 0 + 1.6842105263157894 * (slices of beef) + 0.95 * (tbsp peanut butter)

sandwich_data  = Matrix(elements = [[1,0,0],[1,1,0],[1,2,0],[1,4,0],[1,6,0],[1,0,2],[1,0,4],[1,0,6],[1,0,8],[1,2,2],[1,3,4]])
sandwich_results = Matrix(elements = [[1],[2],[4],[8],[9],[2],[5],[7],[6],[0],[0]])

def regress(Inputs,Results):
    x_tpose = Inputs.transpose()
    return ((x_tpose @ Inputs).inverse() @ (x_tpose @ Results)).elements

betas = regress(sandwich_data,sandwich_results)
rating = str(betas[0][0]) +" + "+ str(betas[1][0])+" * (slices of beef) "+ str(betas[2][0])+" * (tbsp peanut butter)"
print("\n Formula for rating of sandwich:")
print("\n   "+str(rating))
def evaluate(coefficients,coords):
    return coefficients[0]+coefficients[1]*coords[0]+coefficients[2]*coords[1]
print("\n Rating of Sandwich with 5 slices Roast Beef and 0 Tablespoons Peanut Butter:")
print("\n   Rating: "+str(evaluate([betas[0][0],betas[1][0],betas[2][0]],[5,0])))
print("\n Rating of Sandwich with 5 slices Roast Beef and 5 Tablespoons Peanut Butter:")
print("\n  Rating: "+str(evaluate([betas[0][0],betas[1][0],betas[2][0]],[5,5])))

#No, because this estimation is innacurate because the sample data had no samples with roast beef and peanut butter and thus it cannot estimate the quality of a sandwich with both.