class Node():
  def __init__(self, value, next_node=None):
      self.value = value
      self.next_node = next_node
  def get_next_node(self):
    return self.next_node
  def get_value(self):
    return self.value
  def set_next_node(self,new_node):
    self.next_node = new_node
  def set_value(self, new_value):
    self.value = new_value

class Linked_List():
  def __init__(self):
    self.head_node = None
  def get_head_node(self):
    return self.head_node
  def insert_beginning(self, value):
      new_node = Node(value)
      new_node.set_next_node(self.head_node)
      self.head_node = new_node
  def remove_node(self, value_to_remove):
      node_to_remove = None
      current_node = self.head_node
      if current_node.get_value() == value_to_remove:
          self.head_node = self.head_node.get_next_node()
      while current_node is not None:
          next_node = current_node.get_next_node()
          if next_node.get_value() == value_to_remove:
              current_node.set_next_node(next_node.get_next_node())
              break
          current_node = current_node.get_next_node()
      if node_to_remove is not None:
        current_node.set_next_node(next_node.get_next_node())
        return node_to_remove.get_value()
      return False
  def stringify_list(self):
      string_list = ""
      if self.head_node is None:
          return string_list
      current_node = self.head_node
      while current_node:
          string_list = string_list + str(current_node.get_value()) + "\n"
          current_node = current_node.get_next_node()
      return string_list



def nth_last_node(linked_list, n):
  nth_last_pointer = None
  last_pointer = linked_list.head_node
  count = 1

  while last_pointer:
    last_pointer = last_pointer.get_next_node()
    count += 1
    if count >= n + 1:
      if nth_last_pointer is None:
        nth_last_pointer = linked_list.head_node
      else:
        nth_last_pointer = nth_last_pointer.get_next_node()
  return nth_last_pointer


def generate_test_linked_list():
  linked_list = Linked_List()
  for i in range(50):
    linked_list.insert_beginning(i)
  return linked_list

# Use this to test your code:
test_list = generate_test_linked_list()
print(test_list.stringify_list())
nth_last = nth_last_node(test_list, 2)
print(nth_last.value)