import math
from neuron import Neuron

class NeuralNetwork:
    def __init__(self,weights, activation_types = None,activation_functions = None):
        self.weights = weights
        self.num_nodes = list(set([x for x,y in self.weights]+[y for x,y in self.weights]))
        if activation_functions is None:
            self.activation_types = ['linear' for _ in self.num_nodes]
            self.activation_functions = {'linear':{'function':lambda x: x,'derivative':lambda x: 1} for _ in self.num_nodes};
        else:
            self.activation_types = activation_types
            self.activation_functions = activation_functions

        self.nodes = [
            Neuron(self.activation_functions[self.activation_types[i]]['function'],self.activation_functions[self.activation_types[i]]['derivative']) 
        for i in list(set([x for x,y in self.weights]))
        ]+[
            Neuron(self.activation_functions[self.activation_types[i]]['function'],self.activation_functions[self.activation_types[i]]['derivative'], 'output')
         for i in list(set([y for x,y in self.weights]))]

        self.inputs =  [neuron for neuron in self.nodes if neuron.type == 'input']
        self.outputs = [neuron for neuron in self.nodes if neuron.type == 'output']

    def predict(self,inputs):
        sum = 0
        for x,y in self.weights:
            if self.nodes[y] in self.outputs:
                sum += self.nodes[x].activity(inputs[x])*self.weights[(x,y)]

        return self.outputs[0].activity(sum)

    def calc_squared_error(self, data_point):
        return (data_point['output'][0] - self.predict(data_point['input']))**2

    def calc_gradient(self, data_point):
        result = {edge:0 for edge in self.weights}
        delta_y = (self.predict(data_point['input'])- data_point['output'][0])
        output_activity = self.find_output_activity(data_point['input'])
        dy = self.outputs[0].activation_derivative(output_activity) 
        for edge in self.weights:
            result[edge] = 2*(delta_y) * dy*self.nodes[edge[0]].activity(data_point['input'][edge[0]])
        return result

    def find_output_activity(self, inputs):
        sum = 0
        for x,y in self.weights:
            if self.nodes[y] in self.outputs:
                sum += self.nodes[x].activity(inputs[x])*self.weights[(x,y)]
    
        return sum

    def update_weights(self,data_point, learning_rate = 0.01):
        gradient = self.calc_gradient(data_point)
        new_weights = {key:self.weights[key] - (learning_rate * gradient[key]) for key in self.weights}
        self.weights = new_weights


weights = {(0,2): -0.1, (1,2): 0.5}

def linear_function(x):
        return x
def linear_derivative(x):
        return 1
def sigmoidal_function(x):
        return 1/(1+math.exp(-x))
def sigmoidal_derivative(x):
        s = sigmoidal_function(x)
        return s * (1 - s)

activation_types = ['linear', 'linear', 'sigmoidal']
activation_functions = {
    'linear': {
        'function': linear_function,
        'derivative': linear_derivative
    },
    'sigmoidal': {
        'function': sigmoidal_function,
        'derivative': sigmoidal_derivative
    }
}

nn = NeuralNetwork(weights, activation_types, activation_functions)
print(nn.predict([1,0]))
data_points = [
    {'input': [1,0], 'output': [0.1]},
    {'input': [1,1], 'output': [0.2]},
    {'input': [1,2], 'output': [0.4]},
    {'input': [1,3], 'output': [0.7]}
    ]
for i in range(1,10001):
        err = 0
        for data_point in data_points:
            nn.update_weights(data_point)
            err += nn.calc_squared_error(data_point)
        if i < 5 or i % 1000 == 0:
            print('iteration {}'.format(i))
            print('    gradient: {}'.format(nn.calc_gradient(data_point)))
            print('    updated weights: {}'.format(nn.weights))
            print('    error: {}'.format(err))
            print()