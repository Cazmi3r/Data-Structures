class Node():
    def __init__(self, value, next_node = None):
        self.value = value
        self.next_node = next_node
    def set_value(self, new_value):
        self.value = new_value
    def get_value(self):
        return self.value
    def set_next_node(self, new_node):
        self.next_node = new_node
    def get_next_node(self):
        return self.next_node
class Queue():
    def __init__(self):
        
        self.head_node = None

    def enqueue(self, value): # and something to the queue

        new_node = Node(value)
        current_node = self.head_node

        if current_node == None:
            self.head_node = new_node
            return

        while current_node.get_next_node() != None:
            current_node = current_node.get_next_node()

        current_node.set_next_node(new_node)

    def pop(self): # return the first item in the Queue then remove it

        if self.head_node != None:
            value_to_return = self.head_node.get_value()
            self.head_node = self.head_node.get_next_node()
            return value_to_return 

        return False

    def peek(self): # return the first item in the Queue but don't remove it

        if self.head_node == None:
            return False

        else:
            return self.head_node.get_value()

    def stringify(self): # return queue as a sting

        current_node = self.head_node
        return_string = ""

        if self.head_node == None:
            return "sorry the Queue is empty!"

        while current_node != None:
            return_string = return_string + str(current_node.get_value()) + "\n"
            current_node = current_node.get_next_node()

        return return_string