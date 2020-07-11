from src.GradientDescent import GradientDescent

def single_variable_function(x):
    return (x-1)**2
def two_variable_function(x, y):
    return (x-1)**2 + (y-1)**3
def three_variable_function(x, y, z):
    return (x-1)**2 + (y-1)**3 + (z-1)**4
def six_variable_function(x1, x2, x3, x4, x5, x6):
    return (x1-1)**2 + (x2-1)**3 + (x3-1)**4 + x4 + 2*x5 + 3*x6



single_results = [[-2.0000000000000018], [0.0020000000000000018]]
double_results = [[-2.0000000000000018, 3.0001000000000055], [0.0020000000000000018, -0.0030001000000000055]]
triple_results = [[-2.0000000000000018, 3.0001000000000055, -4.0004000000000035], [0.0020000000000000018, -0.0030001000000000055, 0.004000400000000004]]
sextouple_results = [[-2.0000000000000018, 3.0001000000000055, -4.0004000000000035, 1.0000000000000009, 2.0000000000000018, 3.0000000000000027], [0.0020000000000000018, -0.0030001000000000055, 0.004000400000000004, -0.0010000000000000009, -0.0020000000000000018, -0.0030000000000000027]]

funcs = [[single_variable_function, single_results], [two_variable_function, double_results], [three_variable_function, triple_results], [six_variable_function, sextouple_results]]

for f in funcs:
    variable_func = f[0]
    minimizer = GradientDescent(variable_func)
    gradient = minimizer.compute_gradient(delta = 0.01)
    minimizer.descend(scaling_factor=0.001, delta=0.01, num_steps=1)
    minimum = minimizer.minimum
    outputs = [gradient, minimum]

    actual_output = outputs
    desired_output = f[1]
    error_message_gradient = 'incorrect gradient for {}'.format(variable_func.__name__)
    error_message_minimum = 'incorrect minimum for {}'.format(variable_func.__name__)
    details_gradient = '\nOUTPUT: {}\nDESIRED: {}'.format(actual_output[0], desired_output[0])
    details_minimum = '\nOUTPUT: {}\nDESIRED: {}'.format(actual_output[1], desired_output[1])
    assert actual_output[0] == desired_output[0], error_message_gradient + details_gradient
    assert actual_output[1] == desired_output[1], error_message_minimum + details_minimum