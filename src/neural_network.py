import math

class NeuralNetwork:
    def __init__(self,weights, activation_functions = None):
        self.weights = weights
        if activation_functions is None:
            self.activation_functions = [lambda x: x for _ in list(set([x for x,y in self.weights]+[y for x,y in self.weights]))];
        else:
            self.activation_functions = activation_functions
        self.vertices = {x:0 for x in list(set([x for x,y in self.weights]+[y for x,y in self.weights]))}
        self.inputs = list(set([x for x,y in weights]))
        self.output = list(set([y for x,y in weights]))[0]

    def predict(self,inputs):
        for i in range(len(inputs)):
            self.vertices[self.inputs[i]] = inputs[i]

        sum = 0
        for x,y in self.weights:
            if y == self.output:
                sum += self.vertices[x]*self.weights[(x,y)]

        return sum

    def calc_squared_error(self, data_point):
        return (data_point['output'][0] - self.predict(data_point['input']))**2

    def calc_gradient(self, data_point):
        result = {edge:0 for edge in self.weights}
        for edge in self.weights:
            result[edge] = -2*(data_point['output'][0] - self.predict(data_point['input'])) * data_point['input'][edge[0]]
        return result

    def update_weights(self,data_point, learning_rate = 0.01):
        gradient = self.calc_gradient(data_point)
        new_weights = {key:self.weights[key] - (learning_rate * gradient[key]) for key in self.weights}
        self.weights = new_weights


weights = {(0,2): -0.1, (1,2): 0.5}

def linear_activation(x):
    return x
def sigmoidal_activation(x):
    return 1/(1+math.exp(-x))

activation_functions = [linear_activation, linear_activation, sigmoidal_activation]

nn = NeuralNetwork(weights, activation_functions)

data_points = [
    {'input': [1,0], 'output': [0.2689]},
    {'input': [1,1], 'output': [0.0474]},
    {'input': [1,2], 'output': [0.0067]},
    {'input': [1,3], 'output': [0.0009]}
    ]
for _ in range(1000):
        for data_point in data_points:
            nn.update_weights(data_point)

print(nn.weights)