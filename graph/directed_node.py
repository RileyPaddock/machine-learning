class Directed_Node:
    def __init__(self,index):
        self.index = index
        self.value = None
        self.parents = []
        self.children = []
        self.previous = None

    def set_value(self,new_value):
        self.value = new_value
