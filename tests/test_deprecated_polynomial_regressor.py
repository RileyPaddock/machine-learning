import sys
sys.path.append('src')
from polynomial_regressor import PolynomialRegressor

data = [(0,1), (1,2), (2,5), (3,10), (4,20), (5,30)]
correct_results = [[[11.333333333333332], 11.333333333333332],
[[-3.2380952380952412, 5.828571428571428], 8.419047619047616],
[[1.107142857142763, -0.6892857142856474, 1.3035714285714226], 4.942857142857159],
[[1.1349206349217873, -0.8161375661377197, 1.3730158730155861, -0.009259259259233155],4.920634920634827],
[[0.9999999917480108, -2.950000002085698, 6.9583333345161265, -3.9583333337779045, 1.0416666667658463, -0.09166666667401097],4.999999990103076]]
degrees = [0,1,2,3,5]




for i in degrees:
    constant_regressor = PolynomialRegressor(degree=i)
    constant_regressor.ingest_data(data)
    constant_regressor.solve_coefficients()
    output = [constant_regressor.coefficients, constant_regressor.evaluate(2)]
    desired = correct_results[degrees.index(i)]
    rounded_outputs = []
    for coefficient in output[0]:
        rounded_outputs.append(round(coefficient,6))
    rounded_desired = []
    for coefficient in desired[0]:
        rounded_desired.append(round(coefficient,6))

    error_message_coefficients = 'incorrect coefficients for degree ' + str(i)
    error_message_evaluate = 'incorrect evaluation for degree ' + str(i)
    details_coefficients = '\nOUTPUT:  {}\nDESIRED: {}'.format(rounded_outputs, rounded_desired)
    details_evaluate = '\nOUTPUT: {}\nDESIRED: {}'.format(round(output[1],10), round(desired[1],10))
    print("\nTesting coefficieents for degree " + str(i))
    assert rounded_outputs == rounded_desired, error_message_coefficients + details_coefficients
    print("Passed")
    print("\nTesting evaluation for degree " + str(i))
    assert round(output[1],6) == round(desired[1],6), error_message_evaluate + details_evaluate
    print("Passed")

# constant_regressor = PolynomialRegressor(degree=0)
# constant_regressor.ingest_data(data)
# constant_regressor.solve_coefficients()
# constant_regressor.coefficients
# #[11.333333333333332]
# constant_regressor.evaluate(2)
# #11.333333333333332
 
# linear_regressor = PolynomialRegressor(degree=1)
# linear_regressor.ingest_data(data)
# linear_regressor.solve_coefficients()
# print(linear_regressor.coefficients)
# #[-3.2380952380952412, 5.828571428571428]
# linear_regressor.evaluate(2)
# #8.419047619047616
 
# quadratic_regressor = PolynomialRegressor(degree=2)
# quadratic_regressor.ingest_data(data)
# quadratic_regressor.solve_coefficients()
# quadratic_regressor.coefficients
# #[1.107142857142763, -0.6892857142856474, 1.3035714285714226]
# quadratic_regressor.evaluate(2)
# #4.942857142857159
 
# cubic_regressor = PolynomialRegressor(degree=3)
# cubic_regressor.ingest_data(data)
# cubic_regressor.solve_coefficients()
# cubic_regressor.coefficients
# #[1.1349206349217873, -0.8161375661377197, 1.3730158730155861, -0.009259259259233155]
# cubic_regressor.evaluate(2)
# #4.920634920634827
 
# sixth_degree_regressor = PolynomialRegressor(degree=6)
# sixth_degree_regressor.ingest_data(data)
# sixth_degree_regressor.solve_coefficients()
# sixth_degree_regressor.coefficients
# #[195.68690744592448, -54.36653253732979, 7.604147856580724, -4.42417415895568, 1.9296907565114303, -0.28297710478739835, 0.014172483987375945]
# sixth_degree_regressor.evaluate(2)
# #104.70386425212057