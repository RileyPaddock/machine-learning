class Tree:
    def __init__(self, head_value = None):
        self.root = None
        self.data = []

    def build_from_edges(self, edges):
        self.set_root(edges)
        layer_nodes = [self.root]
        self.set_children(self.root, edges)

        while len(layer_nodes) > 0:
            next_layer_nodes = self.get_layer_children(layer_nodes)
            self.set_layer_children(next_layer_nodes, edges)
            layer_nodes = next_layer_nodes

    def print_depth_first(self, node):
        print(node.data)
        for child in node.children:
            self.print_depth_first(child)

    def insert(self, tree, node):
        tree.root.parent = node
     
    def breadth_first_traversal(self, queue):
        values_in_layer = 0

        for i in range(0, len(queue)):#prints data of one layer
            values_in_layer = i
            self.data.append(queue[i].data)

        children_arr = [child for parent in queue for child in parent.children]#adds the next layer to the queue
        for child in children_arr:
            if child != None:
                queue.append(child)
        
        if len(queue) > 0:#removes the layer already printed and checks for last layer
            for i in range(0, values_in_layer + 1):
                queue.remove(queue[0])
            return self.breadth_first_traversal(queue)


    def get_layer_children(self, layer_nodes):
        return [child for parent in layer_nodes for child in parent.children]

    def set_layer_children(self, layer_nodes,edges):
        for node in layer_nodes:
            self.set_children(node, edges)

    def set_root(self, edges):
        for parent,child in edges:
            root_count = 0
            for parent_check,child_check in edges:
                if parent == child_check:
                    root_count = 0
                else:
                    root_count += 1
            if root_count == len(edges):
                self.root = Node(parent)

    
    def set_children(self, node, edges):    
        children_from_edges = [Node(child) for parent,child in edges if parent == node.data]
        node.children = [child for child in children_from_edges if child not in node.children]

class Node:
    def __init__(self, value):
        self.data = value
        self.children = []
        self.parent = None