import sys
sys.path.append('src')
from matrix import Matrix

sandwich_data  = Matrix(elements = [[1,0,0],[1,1,0],[1,2,0],[1,4,0],[1,6,0],[1,0,2],[1,0,4],[1,0,6],[1,0,8],[1,2,2],[1,3,4]])
sandwich_results = Matrix(elements = [[1],[2],[4],[8],[9],[2],[5],[7],[6],[0],[0]])

def regress(Inputs,Results):
    x_tpose = Inputs.transpose()
    return ((x_tpose @ Inputs).inverse() @ (x_tpose @ Results)).elements

betas = regress(sandwich_data,sandwich_results)

# QUESTION 1
# What is the model?
 
#    rating = 1.5873900293255154 + 0.8671554252199407 * (slices of beef) 0.4203812316715543 * (tbsp peanut butter)
 
# QUESTION 2
# What is the predicted rating of a sandwich with 5 slices of roast beef AND 
# 5 tablespoons of peanut butter (on the same sandwich)?
 
#    8.02507331378299
 
# QUESTION 3
# How does this prediction compare to that from the previous assignment? Did 
# including the additional data make the prediction trustworthy? Why or why not?
 
#   It did not make the prediction trustworthy because while the estimate is still lower than the original due to the new data it is still innaccurate. This is due to the fact that an equation of this type cannot represent data with 3 possiblilities. It cannot accuratley express a rating for a sandwich with both ingredients without lowering the rating for each individual ingradient which defies the data.



sandwich_data  = Matrix(elements = [[1,0,0,0],[1,1,0,0],[1,2,0,0],[1,4,0,0],[1,6,0,0],[1,0,2,0],[1,0,4,0],[1,0,6,0],[1,0,8,0],[1,2,2,4],[1,3,4,12]])
sandwich_results = Matrix(elements = [[1],[2],[4],[8],[9],[2],[5],[7],[6],[0],[0]])

betas = regress(sandwich_data,sandwich_results)
rating = str(betas[0][0]) +" + "+ str(betas[1][0])+" * (slices of beef) "+ str(betas[2][0])+" * (tbsp peanut butter)" + str(betas[3][0])+" * (slices of beef)(tbsp peanut butter)" 
print("\n Formula for rating of sandwich:")
print("\n   "+str(rating))
def evaluate(coefficients,coords):
    return coefficients[0]+coefficients[1]*coords[0]+coefficients[2]*coords[1] + coefficients[3]*(coords[0]*coords[1])
print("\n Rating of Sandwich with 5 slices Roast Beef and 0 Tablespoons Peanut Butter:")
print("\n   Rating: "+str(evaluate([betas[0][0],betas[1][0],betas[2][0],betas[3][0]],[5,0])))
print("\n Rating of Sandwich with 5 slices Roast Beef and 5 Tablespoons Peanut Butter:")
print("\n  Rating: "+str(evaluate([betas[0][0],betas[1][0],betas[2][0],betas[3][0]],[5,5])))

# QUESTION 4
# Fill out the table with the additional interaction term:
 
# (slices beef) | (tbsp peanut butter) | (slices beef)(tbsp peanut butter) | Rating |
# -----------------------------------------------------------------------------------
#       0       |           0          |                 0                 |    1   |
#       1       |           0          |                 0                 |    2   |
#       2       |           0          |                 0                 |    4   |
#       4       |           0          |                 0                 |    8   |
#       6       |           0          |                 0                 |    9   |
#       0       |           2          |                 0                 |    2   |
#       0       |           4          |                 0                 |    5   |
#       0       |           6          |                 0                 |    7   |
#       0       |           8          |                 0                 |    6   |
#       2       |           2          |                 4                 |    0   | 
#       3       |           4          |                 12                |    0   |
 
# QUESTION 5
# What is the system of equations?
 
#   1 * beta_0 + 0 * beta_1 + 0 * beta_2 + 0 * beta_3 = 1
#   1 * beta_0 + 1 * beta_1 + 0 * beta_2 + 0 * beta_3 = 2
#   1 * beta_0 + 2 * beta_1 + 0 * beta_2 + 0 * beta_3 = 4
#   1 * beta_0 + 4 * beta_1 + 0 * beta_2 + 0 * beta_3 = 8
#   1 * beta_0 + 6 * beta_1 + 0 * beta_2 + 0 * beta_3 = 9
#   1 * beta_0 + 0 * beta_1 + 2 * beta_2 + 0 * beta_3 = 2
#   1 * beta_0 + 0 * beta_1 + 4 * beta_2 + 0 * beta_3 = 5
#   1 * beta_0 + 0 * beta_1 + 6 * beta_2 + 0 * beta_3 = 7
#   1 * beta_0 + 0 * beta_1 + 8 * beta_2 + 0 * beta_3 = 6
#   1 * beta_0 + 2 * beta_1 + 2 * beta_2 + 4 * beta_3 = 0
#   1 * beta_0 + 3 * beta_1 + 4 * beta_2 + 12 * beta_3 = 0
 
# QUESTION 6
# What is the matrix equation?
 
#   [[1, 0, 0, 0],                   [[1],
#    [1, 1, 0, 0],                    [2],
#    [1, 2, 0, 0],                    [4],
#    [1, 4, 0, 0],    [[beta_0],      [8],
#    [1, 6, 0, 0],     [beta_1],  =   [9],     
#    [1, 0, 2, 0],     [beta_2],      [2],
#    [1, 0, 4, 0],     [beta_3]]      [5],
#    [1, 0, 6, 0],                    [7],
#    [1, 0, 8, 0],                    [6],
#    [1, 2, 2, 4],                    [0],
#    [1, 3, 4, 12],                    [0]
 
# QUESTION 7
# What is the model?
 
#    rating = 0.8707473221980564 + 1.445294866007305 * (slices beef) + 0.7921061271391636 * (tbsp peanut butter) + -0.7617679648705218 * (slices beef)(tbsp peanut butter)
 
# QUESTION 8
# What is the predicted rating of a sandwich with 5 slices of roast beef AND 
# 5 tablespoons of peanut butter (on the same sandwich)?
 
#    -6.986446833832643
 
# QUESTION 9
# How does this prediction compare to that from the previous assignment? Did 
# including interaction term make the prediction trustworthy? Why or why not?
 
#    This prediction is better than that of the previous assignment because it still gives an accurate rating to a sandwich with only one topping but it lowers the rating of a sandwich with both toppings. The interaction term makes this equation trustworthy because it shows that sandwiches with both toppings are bad.