
class NeuralNetwork:
    def __init__(self,weights):
        self.weights = weights
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
        for i in range(len(data_point['input'])):
            self.vertices[self.inputs[i]] = data_point['input'][i]

        result = {edge:0 for edge in self.weights}
        for edge in self.weights:
            result[edge] = -2*(data_point['output'][0] - self.predict(data_point['input'])) * data_point['input'][edge[0]]

        return result

    def update_weights(self,data_point, learning_rate = 0.01):
        gradient = self.calc_gradient(data_point)
        new_weights = {key:self.weights[key] - (learning_rate * gradient[key]) for key in self.weights}
        self.weights = new_weights


weights = {(0,2): -0.1, (1,2): 0.5}
nn = NeuralNetwork(weights)
data_points = [
    {'input': [1,0], 'output': [1]},
    {'input': [1,1], 'output': [3]},
    {'input': [1,2], 'output': [5]},
    {'input': [1,3], 'output': [7]}
    ]

for _ in range(1000):
    for data_point in data_points:
        nn.update_weights(data_point)

print(nn.weights)