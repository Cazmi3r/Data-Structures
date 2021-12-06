from Doubly_Linked_List import Doubly_Linked_List

ll = Doubly_Linked_List()

# Set_prev_node
print("_____Doubly_Linked_List_____")

print("-----add_to_head-----")
# add to an empty list
ll.add_to_head(3)
# add to list with one element
ll.add_to_head(2)
# add to list with more than one element
ll.add_to_head(1)
print(ll.stringify_list())

print("-----add_to_tail-----")
ll = Doubly_Linked_List()
# add to an empty list
ll.add_to_tail(1)
# add to list with one element
ll.add_to_tail(2)
# add to list with more than one element
ll.add_to_tail(3)
print(ll.stringify_list())

print("-----remove_head-----")
# remove from list with more than 2 elements
ll.remove_head()
# remove from list with 2 elements
ll.remove_head()
ll.remove_head()
ll.remove_head()
print(ll.stringify_list())

print("------remove_tail------")

ll = Doubly_Linked_List()
ll.add_to_head(1)
ll.add_to_tail(2)
ll.add_to_tail(3)
ll.remove_tail()
ll.remove_tail()
ll.remove_tail()
ll.remove_tail()
print(ll.stringify_list())
