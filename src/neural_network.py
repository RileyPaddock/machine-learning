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
        for i in self.num_nodes]
        self.nodes[-1].type = 'output'

        self.inputs =  [neuron for neuron in self.nodes if neuron.type == 'input']
        self.outputs = [neuron for neuron in self.nodes if neuron.type == 'output']
        self.final_output = self.outputs[-1]

    def predict(self,inputs):
        return self.final_output.activity(self.i(len(self.nodes)-1,inputs))

    def calc_squared_error(self, data_point):
        return (data_point['output'][0] - self.predict(data_point['input']))**2

    def calc_gradient(self, data_point):
        result = {edge:self.dE_dw(edge,data_point) for edge in self.weights}
        print("\tdw_01 = "+str(round(result[(0,1)],4))+", dw_12 = "+str(round(result[(1,2)],4)))
        return result

    def dE_dw(self,stop_edge,data_point):
        edge_path = [[key for key in self.weights][-1]]
        while edge_path[-1][0] != stop_edge[0]:
            for edge in self.weights:
                if edge[1] == edge_path[-1][0]:
                    edge_path.append(edge)
        result = self.dE_start(data_point)
        for edge in edge_path:
            if edge == stop_edge:
                if edge[0] == 0:
                    result *= self.nodes[edge[0]].activity(data_point['input'][0])
                else:
                    result *= self.nodes[edge[0]].activity(self.i(edge[0],data_point['input']))
            else:
                result *= self.weights[edge]*self.nodes[edge[0]].activation_derivative(self.i(edge[0],data_point['input']))
        return result
    
    def i(self,node,input,result = 1):
        edges = [edge for edge in self.weights if edge[1] == node]
        for edge in edges:
            if edge[0]==0:
                result = self.weights[edge]*self.nodes[0].activity(input[0])
            else:
                result *= self.weights[edge]*self.nodes[edge[0]].activity(self.i(edge[0],input,result))
        return result


    def dE_start(self,data_point):
        output_i = len(self.nodes)-1
        delta_y = (self.final_output.activity(self.i(output_i,data_point['input']))- data_point['output'][0])
        output_activity = self.i(output_i,data_point['input'])
        dy = self.final_output.activation_derivative(output_activity) 

        return 2 * (delta_y) * dy


    def update_weights(self,data_point, learning_rate = 0.001):
        gradient = self.calc_gradient(data_point)
        new_weights = {key:self.weights[key] - (learning_rate * gradient[key]) for key in self.weights}
        self.weights = new_weights
        print("\tw_01 = "+str(round(self.weights[(0,1)],4))+", w_12 = "+str(round(self.weights[(1,2)],4)))


weights = {(0,1): 1, (1,2): 1}

def linear_function(x):
        return x
def linear_derivative(x):
        return 1
def sigmoidal_function(x):
        return 1/(1+math.exp(-x))
def sigmoidal_derivative(x):
        s = sigmoidal_function(x)
        return s * (1 - s)
def sin(x):
    return math.sin(x)
def sin_derivative(x):
    return math.cos(x)

activation_types = ['linear', 'sin', 'linear']
activation_functions = {
    'linear': {
        'function': linear_function,
        'derivative': linear_derivative
    },
    'sin': {
        'function': sin,
        'derivative': sin_derivative
    }
}

nn = NeuralNetwork(weights, activation_types, activation_functions)

data_points = [
    {'input': [1,0], 'output': [0.1]},
    {'input': [1,1], 'output': [0.2]},
    {'input': [1,2], 'output': [0.4]},
    {'input': [1,3], 'output': [0.7]}
    ]
data_points = [{'input': [0],'output': [0.0]},
 {'input': [1], 'output':[1.44]},
 {'input': [2], 'output':[2.52]},
 {'input': [3], 'output':[2.99]},
 {'input': [4], 'output':[2.73]},
 {'input': [5], 'output':[1.8]},
 {'input': [6], 'output':[0.42]},
 {'input': [7], 'output':[-1.0]},
 {'input': [8], 'output':[-2.27]},
 {'input': [9], 'output':[-2.93]},
 {'input': [10], 'output':[-2.88]},
 {'input': [11], 'output':[-2.12]},
 {'input': [12], 'output':[-0.84]},
 {'input': [13], 'output':[0.65]},
 {'input': [14], 'output':[1.97]},
 {'input': [15], 'output':[2.81]},
 {'input': [16], 'output':[2.97]},
 {'input': [17], 'output':[2.4]},
 {'input': [18], 'output':[1.24]},
 {'input': [19], 'output':[-0.23]}]

for i in range(1,1000):
    
    err = 0
    for data_point in data_points:
        print('loop '+str(i)+', point '+str((data_point['input'][0],data_point['output'][0])))
        nn.update_weights(data_point)
        err += nn.calc_squared_error(data_point)
        
        
        print('\n')

print(nn.weights)