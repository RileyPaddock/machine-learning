Import sys
sys.path.append('graph')
from graph import Graph
class WeightedGraph:
    def __init__(self, weights, vertices):
        self.weights = weights
        self.vertices = {i:vertices[i] for i in range(len(vertices))}
        self.dvalues = {x:99999 for x in list(set([x for x,y in self.weights]+[y for x,y in self.weights]))}


    def calc_dvalues(self,current, queue = [],visited = [], start = True):
        if start == True: 
            self.dvalues[current] = 0 
            queue.append(current)

        for x,y in self.weights:
            if x == current:
                if self.dvalues[x]+self.weights[(x,y)] < self.dvalues[y]:
                    self.dvalues[y] = self.dvalues[x]+self.weights[(x,y)]
            elif y == current:
                if self.dvalues[y]+self.weights[(x,y)] < self.dvalues[x]:
                    self.dvalues[x] = self.dvalues[y]+self.weights[(x,y)]
        visited.append(current)
        queue.remove(current)

        if len(visited) == len(list(set([x for x,y in self.weights]+[y for x,y in self.weights]))):
            return
        else:
            connected_dvalues = [y for x,y in self.weights if x == current and y not in visited]+[x for x,y in self.weights if y == current and x not in visited]

            for neighbors in connected_dvalues:
                queue.append(neighbors)
            if connected_dvalues != []:
                return self.calc_dvalues(min([(self.dvalues[x],x) for x in connected_dvalues])[1],queue, visited, False)
            else:
                return self.calc_dvalues(queue[0],queue, visited, False)

    def calc_distance(self,start, end):
        self.dvalues = {x:99999 for x in list(set([x for x,y in self.weights]+[y for x,y in self.weights]))}
        self.calc_dvalues(start, [],[],True)
        return self.dvalues[end]
        
    def calc_shortest_path(self, start, end):
        self.calc_dvalues(start, [], [], True)
        shortest_path_graph = self.build_shortest_path_graph(start, end)
        return shortest_path_graph.calc_shortest_path(start, end)

    def build_shortest_path_graph(self,start, end):
        edges = []
        active = start
        queue = [start]

        while active != end:
            connections = [(x,y) for x,y in self.weights if x == active]+[(x,y) for x,y in self.weights if y == active]
            for connection in connections:
                if active == connection[0]:
                    if self.dvalues[active] + self.weights[(active,connection[1])] == self.dvalues[connection[1]]:
                        edges.append((active,connection[1])) 
                        queue.append(connection[1])
                else:
                    if self.dvalues[active]+self.weights[(connection[0], active)] == self.dvalues[connection[0]]:
                        edges.append((connection[0], active))
                        queue.append(connection[0])
            del queue[0]
            active = queue[0]

        return Graph(edges, self.vertices)
            
    



weights = {
    (0,1): 3,
    (1,7): 4,
    (7,2): 2,
    (2,5): 1,
    (5,6): 8,
    (0,3): 2,
    (3,2): 6,
    (3,4): 1,
    (4,8): 8,
    (8,0): 4
}
vertex_values = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
weighted_graph = WeightedGraph(weights, vertex_values)

print("Testing Shortest Path")
assert weighted_graph.calc_shortest_path(8,4) == [8, 0, 3, 4]

assert weighted_graph.calc_shortest_path(8,7) == [8, 0, 1, 7]

assert weighted_graph.calc_shortest_path(8,6) == [8, 0, 3, 2, 5, 6]
print("     passed")

print("\nTesting distance")
assert weighted_graph.calc_distance(8,4) == 7

assert [weighted_graph.calc_distance(8,n) for n in range(9)] == [4, 7, 12, 6, 7, 13, 21, 11, 0]
print("     passed")