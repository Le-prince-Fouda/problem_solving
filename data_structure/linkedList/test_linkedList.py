from linkedList import LinkedList

l1 = LinkedList()
print("Is empty?", l1.is_empty())

# Insert 10 elements into the linked list
for i in range(10):
    l1.add_tail(i)

l1.print_list()
l1.print_head_tail()
print()

print("Length:", l1.get_size())
print("Is empty?", l1.is_empty())
print("Node at index 5:", l1.get_node(5))

print()
print("Add the value 50 at index 5")
l1.insert_at_position(5, 50)
l1.print_list()
l1.print_head_tail()
#####

print()
print("Remove 50")
l1.remove(50)
l1.print_list()
l1.print_head_tail()

print()
print("Add 11 and 10")
l1.add_tail( 11)
l1.add_tail( 10)
l1.print_list()
l1.print_head_tail()

print()
print("Insert 10 after 5")
l1.add_head( 10)
l1.print_list()
l1.print_head_tail()
#######

print()
print("Remove the 10 after 5")
l1.remove_by_index(6)
l1.print_list()
l1.print_head_tail()

print()
print("Remove 9, 10, and 11")
l1.remove(9)
l1.remove_tail()
l1.remove_tail()
l1.print_list()
l1.print_head_tail()

print()
print("Remove 0")
l1.remove(0)
l1.print_list()
l1.print_head_tail()
# #######

print("Length:", l1.get_size())
print()
print("Remove all elements from 1 to 5 inclusive.")
# Remove the element at index 1 five times
for _ in range(5):
    l1.remove_by_index(1)
l1.print_list()
l1.print_head_tail()

print()
print("Remove the first element")
l1.remove_head()
l1.print_list()
l1.print_head_tail()

print()
print("Remove the first element")
l1.remove_head()
l1.print_list()
l1.print_head_tail()
print("Length:", l1.get_size())


print()
print("Remove the first element")
l1.remove_head()
l1.print_list()
l1.print_head_tail()
print("Length:", l1.get_size())

