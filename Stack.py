class Node():
    def __init__(self, value, next_node = None):
        self.value = value
        self.next_node = next_node
    def get_value(self):
        return self.value
    def set_value(self, new_value):
         self.value = new_value
    def get_next_node(self):
        return self.next_node
    def set_next_node(self, new_node):
        self.next_node = new_node

class Stack():
    def __init__(self, name, limit = 999):
        self.name = name
        self.limit = limit
        self.size = 0
        self.head_node = None
    def get_name(self):
        return self.name
    def get_size(self):
        return self.size
    def is_empty(self):
        return self.size == 0
    def push(self, new_value):
        new_node = Node(new_value)
        if self.is_empty():
            self.head_node = new_node
        else:
            new_node.set_next_node(self.head_node)
            self.head_node = new_node
        self.size += 1
    def peek(self):
        if self.is_empty():
            return "Empty"
        return self.head_node.get_value()
    def pop(self):
        if self.is_empty():
            return False
        else:
            node_to_remove = self.head_node
            self.head_node = self.head_node.get_next_node()
            self.size += -1
            return node_to_remove.get_value()
    def print_items(self):
        if self.is_empty():
            return "0"
        else:
            return_string = ""
            current_node = self.head_node
            while current_node is not None:
                return_string += "{}".format(current_node.get_value())
                current_node = current_node.get_next_node()
            return return_string
