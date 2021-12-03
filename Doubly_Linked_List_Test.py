from Doubly_Linked_List import Doubly_Linked_List

ll = Doubly_Linked_List()

# Set_prev_node
print("_____Doubly_Linked_List_____")

print("-----add_to_head-----")
# add to an empty list
ll.add_to_head(2)
# add to list with one element
ll.add_to_head(1)
print(ll.stringify_list())
