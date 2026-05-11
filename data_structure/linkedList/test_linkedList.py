from linkedList import LinkedList

l1 = LinkedList()
print("Est vide?", l1.is_empty())

#On insère 10 éléments dans la liste chaînée
for i in range(10):
    l1.add_tail(i)

l1.print_list()
l1.print_head_tail()
print()

print("Longueur :", l1.get_size())
print("Est vide?", l1.is_empty())
print("Noeud à l'indice 5 :", l1.get_node(5))

print()
print("On ajoute la valeur 50 à l'indice 5")
l1.insert_at_position(5, 50)
l1.print_list()
l1.print_head_tail()
#####

print()
print("On retire le 50")
l1.remove(50)
l1.print_list()
l1.print_head_tail()

print()
print("On ajoute le 11 et le 10")
l1.add_tail( 11)
l1.add_tail( 10)
l1.print_list()
l1.print_head_tail()

print()
print("On insère un 10 après le 5")
l1.add_head( 10)
l1.print_list()
l1.print_head_tail()
#######

print()
print("On retire le 10 après le 5")
l1.remove_by_index(6)
l1.print_list()
l1.print_head_tail()

print()
print("On retire le 9, le 10 et le 11")
l1.remove(9)
l1.remove_tail()
l1.remove_tail()
l1.print_list()
l1.print_head_tail()

print()
print("On retire le 0")
l1.remove(0)
l1.print_list()
l1.print_head_tail()
# #######

print("Longueur :", l1.get_size())
print()
print("On retire tous les éléments allant de 1 à 5 inclus.")
# On retire 5 fois l'élément qui se trouve à l'index 1
for _ in range(5):
    l1.remove_by_index(1)
l1.print_list()
l1.print_head_tail()

print()
print("On retire le premier élément")
l1.remove_head()
l1.print_list()
l1.print_head_tail()

print()
print("On retire le premier élément")
l1.remove_head()
l1.print_list()
l1.print_head_tail()
print("Longueur :", l1.get_size())

print()
print("On retire le premier élément")
l1.remove_head()
l1.print_list()
l1.print_head_tail()
print("Longueur :", l1.get_size())

