from src.GradientDescent import GradientDescent

def single_variable_function(x):
    return (x-1)**2
def two_variable_function(x, y):
    return (x-1)**2 + (y-1)**3
def three_variable_function(x, y, z):
    return (x-1)**2 + (y-1)**3 + (z-1)**4
def six_variable_function(x1, x2, x3, x4, x5, x6):
    return (x1-1)**2 + (x2-1)**3 + (x3-1)**4 + x4 + 2*x5 + 3*x6

funcs = [single_variable_function, two_variable_function, three_variable_function, six_variable_function]

single_results = [[-2.0000000000000018], [0.0020000000000000018]]
double_results = [[-2.0000000000000018, 3.0001000000000055], [0.0020000000000000018, -0.0030001000000000055]]
triple_results = [[-2.0000000000000018, 3.0001000000000055, -4.0004000000000035], [0.0020000000000000018, -0.0030001000000000055, 0.004000400000000004]]
sextouple_results = [[-2.0000000000000018, 3.0001000000000055, -4.0004000000000035, 1.0000000000000009, 2.0000000000000018, 3.0000000000000027], [0.0020000000000000018, -0.0030001000000000055, 0.004000400000000004, -0.0010000000000000009, -0.0020000000000000018, -0.0030000000000000027]]

correct_outputs = [single_results, double_results, triple_results, sextouple_results]

for f in funcs:
    minimizer = GradientDescent(f)
    gradient = minimizer.compute_gradient(delta = 0.01)
    minimum = minimizer.descend(scaling_factor=0.001, delta=0.01, num_steps=1)
    outputs = [gradient, minimum]
    for correct_gradient in correct_outputs:
        actual_output = outputs
        desired_output = correct_gradient
        error_message_gradient = 'incorrect gradient for {}'.format(f.__name__)
        error_message_minimum = 'incorrect minimum for {}'.format(f.__name__)
        details_gradient = '\nOUTPUT: {}\nDESIRED: {}'.format(actual_output[0], desired_output[0])
        details_minimum = '\nOUTPUT: {}\nDESIRED: {}'.format(actual_output[1], desired_output[1])
        assert actual_output[0] == desired_output[0], error_message_gradient + details_gradient
        assert actual_output[1] == desired_output[1], error_message_gradient + details_gradient