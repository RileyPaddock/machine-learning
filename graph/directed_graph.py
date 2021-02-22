import sys
sys.path.append('graph')
from directed_node import DirectedNode

class DirectedGraph:
    def __init__(self, edges, verticies = None):
        self.edges = edges
        self.nodes = []
        self.build_from_edges()

    def build_from_edges(self):
        edge_indicies = []
        for x,y in self.edges:
            if x not in edge_indicies:
                edge_indicies.append(x)
            if y not in edge_indicies:
                edge_indicies.append(y)
        for i in edge_indicies:
            self.nodes.append(DirectedNode(i))
        for x,y in self.edges:
            self.nodes[x].children.append(self.nodes[y])
            self.nodes[y].parents.append(self.nodes[x])
        for i in edge_indicies:
            self.nodes[i].value = i
    
    def calc_distance(self,i,j):
        result = []
        queue = [i]
        generation = 0
        if self.nodes[i].children == []:
            return False
        else:
            while self.nodes[j].index not in queue:
                static_len = len(queue)
                for i in range(static_len):
                    for neighbor in self.nodes[queue[0]].children:
                        queue.append(neighbor.index)
                    if queue[0] not in result:
                        result.append(queue[0])
                    queue.remove(queue[0])
                generation += 1
            return generation

    def calc_shortest_path(self,start,end):
        if self.nodes[start].children == []:
            return False
        else:
            self.nodes[start].previous = "done"
            result = [end]
            queue = [start]
            while end not in queue:
                for neighbor in self.nodes[queue[0]].children:
                    if self.nodes[neighbor.index].previous is None:
                        self.nodes[neighbor.index].previous = queue[0]
                    queue.append(neighbor.index)
                queue.remove(queue[0])

            active_node = self.nodes[end]
            while active_node.previous != "done":
                result.append(active_node.previous)
                active_node = self.nodes[active_node.previous]

            result.reverse()
            for node in self.nodes:
                node.previous = None
            return result
