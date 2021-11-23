from Linked_List import Linked_List

print("_____Linked List_____")
print("-----Insert Beginning-----")
ll = Linked_List()
ll.insert_beginning("hello")
ll.insert_beginning("me")
ll.insert_beginning("its")
print(ll.stringify_list())
print("-----Remove Node-----")
# tests if value is not in list
print(ll.remove_node("Im not here"))
#removes node from middle of list
print(ll.remove_node("me"))
#removes node from front of list
ll.remove_node("its")
#removed only node in list
ll.remove_node("hello")
#trys to remove a node from an empty list
ll.remove_node("Empty")
print(ll.stringify_list())
print("------Get Head Node-----")
print(ll.get_head_node())
ll.insert_beginning(3)
print(ll.get_head_node())
ll.insert_beginning(2)
print(ll.get_head_node())
ll.insert_beginning(1)
print(ll.get_head_node())