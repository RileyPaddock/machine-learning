import sys
sys.path.append('graph')
from node import Node
class Graph:
    def __init__(self, edges, vertices):
        self.edges = edges
        self.vertices = vertices
        self.nodes = [Node(i) for i in list(set([x for x,y in edges]+[y for x,y in edges]))]
        self.unique_indices = list(set([x for x,y in self.edges]+[y for x,y in self.edges]))
        self.correct_indices = [x for x in range(len(self.unique_indices))]
        self.set_up_nodes()

    def set_up_nodes(self):
        
        for i in list(set([x for x,y in self.edges]+[y for x,y in self.edges])):
            self.nodes[self.correct_indices[self.unique_indices.index(i)]].value = self.vertices[i]
        for x,y in self.edges:
            self.nodes[self.correct_indices[self.unique_indices.index(x)]].neighbors.append(self.nodes[self.correct_indices[self.unique_indices.index(y)]])

    def depth_first_search(self,starting_index):
        result = [starting_index]
        i = starting_index
        while len(result)<len(self.nodes):
            for node in self.nodes[i].neighbors:
                if node.index not in result:
                    result.append(node.index)
                    i = node.index
        return result
        
    def breadth_first_search(self,starting_index):
        result = []
        queue = [starting_index]
        while len(result) < len(self.nodes):
                for neighbor in self.nodes[queue[0]].neighbors:
                    queue.append(neighbor.index)
                if queue[0] not in result:
                    result.append(queue[0])
                queue.remove(queue[0])
        return result

    def calc_distance(self,i,j):
        result = []
        queue = [i]
        generation = 0
        while self.nodes[j].index not in queue:
            static_len = len(queue)
            for i in range(static_len):
                for neighbor in self.nodes[queue[0]].neighbors:
                    queue.append(neighbor.index)
                if queue[0] not in result:
                    result.append(queue[0])
                queue.remove(queue[0])
            generation += 1
        return generation

    def calc_shortest_path(self,start, end):
        self.nodes[self.correct_indices[self.unique_indices.index(start)]].previous = "done"
        result = [end]
        queue = [self.correct_indices[self.unique_indices.index(start)]]
        while end not in queue:
            for neighbor in self.nodes[queue[0]].neighbors:
                if self.nodes[self.correct_indices[self.unique_indices.index(neighbor.index)]].previous is None:
                    self.nodes[self.correct_indices[self.unique_indices.index(neighbor.index)]].previous = queue[0]
                queue.append(neighbor.index)
            queue.remove(queue[0])

        active_node = self.nodes[self.correct_indices[self.unique_indices.index(end)]]
        while active_node.previous != "done":
            result.append(self.unique_indices[active_node.previous])
            active_node = self.nodes[active_node.previous]

        result.reverse()
        for node in self.nodes:
            node.previous = None
        return result

