class Neuron:
    def __init__(self,value, activation_function, activation_derivative, type_ = 'input'):
        self.value = value
        self.activation_function = activation_function
        self.activation_derivative = activation_derivative
        self.type = type_
        