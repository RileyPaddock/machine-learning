class Neuron:
    def __init__(self, activation_function, activation_derivative, type_ = 'input'):
        self.activation_function = activation_function
        self.activation_derivative = activation_derivative
        self.type = type_
        self.activity = lambda x: self.activation_function(x)