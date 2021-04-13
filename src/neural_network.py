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
        #print("\tdw_01 = "+str(round(result[(0,1)],4))+", dw_12 = "+str(round(result[(1,2)],4)))
        return result

    def dE_dw(self,stop_edge,data_point):
        return self.dE_start(data_point)*self.di_dw(stop_edge,self.num_nodes[-1],data_point)

    def di_dw(self,stop_edge,n,data_point):
        edge_path = self.find_edge_path(stop_edge)
        relevant_edges = [edge for edge in edge_path if edge[1] == n]
        if stop_edge in relevant_edges:
            if stop_edge[0] == 0:
                return self.nodes[stop_edge[0]].activity(data_point['input'][0])
            else:
                return self.nodes[stop_edge[0]].activity(self.i(stop_edge[0],data_point['input']))
        else:
            return sum([self.weights[edge]*self.nodes[edge[0]].activation_derivative(self.i(edge[0],data_point['input']))*self.di_dw(stop_edge,edge[0],data_point) for edge in relevant_edges])

    def find_edge_path(self,stop_edge):
        edge_queue = [stop_edge]
        edge_path = [stop_edge]
        while len(edge_queue)>0:
            for edge in self.weights:
                if edge[0] == edge_queue[0][1] and edge not in edge_path:
                    edge_queue.append(edge)
            if edge_queue[0] not in edge_path:
                edge_path.append(edge_queue[0])
            del edge_queue[0]

        return edge_path[::-1]
    
    def i(self,node,input,result = 1):
        edges = [edge for edge in self.weights if edge[1] == node]
        if len(edges) == 1:
            edge = edges[0]

            if edge[0]==0:
                result = self.weights[edge]*self.nodes[0].activity(input[0])
            else:
                result *= self.weights[edge]*self.nodes[edge[0]].activity(self.i(edge[0],input,result))
        else:
            result = sum([self.weights[edge]*self.nodes[edge[0]].activity(self.i(edge[0],input,result)) for edge in edges])

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
        #print("\tw_01 = "+str(round(self.weights[(0,1)],4))+", w_12 = "+str(round(self.weights[(1,2)],4)))


weights = {(0,1): 1, (1,2): 1, (1,3): 1, (2,4): 1, (3,4): 1}

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

activation_types = ['linear', 'linear', 'linear', 'linear', 'linear']
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


print(nn.dE_dw((0,1),{'input': [1],'output': [1]},))
# for i in range(1,1000):
    
#     err = 0
#     for data_point in data_points:
#         #print('loop '+str(i)+', point '+str((data_point['input'][0],data_point['output'][0])))
#         nn.update_weights(data_point)
#         err += nn.calc_squared_error(data_point)
        
        
#         print('\n')

# print(nn.weights)