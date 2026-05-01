from node import Node

class LinkedList:

    # we initialize a linkedlist without node
    def __init__(self):
        self.node = None
        self.head = None # head/first node of linked list
        self.tail = None #tail/last node of linked list
        self.size = 0    # linked list size


    ############ insertion ##############

    ## add or create the first node (head) of the linked list
    def add_head(self, data):
        new_node = Node(data) # we create the node
        new_node.next = self.head # our node is the previous node of the head of the linked list
        self.head = new_node # now the created node is the first of the linked list
        self.size += 1 # increment the size of the list


    ## This method works in the same way as ‘add_head’, but in this case, an existing node is added as the head node.
    ## add_head create first the node than add it as the head
    def add_node_to_head(self, new_node: Node):
        new_node.next = self.head # our node is the previous node of the head of the linked list
        self.head = new_node # now the created node is the first of the linked list
        self.size += 1 # increment the size of the list



    ## this methode create and add a node as the tail of the linked list
    def add_tail(self, data):
        new_node = Node(data) # we create the node to add

        # case 1: The linkedlist is empty
        #####if...: self.add_head(data); self.tail = self.head
        if self.head is None:
            self.head = new_node
            self.tail = self.head

        # case 2: The linkedlist has one or more nodes
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1 # increment the size of the list



    ## this methode add an existing node as the tail of the linked list
    def add_node_to_tail(self, new_node: Node):
        # case 1: The linkedlist is empty
        ##### reecrire cette condition en utilisant add_node_to_head
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        # case 2: The linkedlist has one or more nodes
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1 # increment the size of the list


    def insert_at_position(self, index, data ):
        #case 1: negative index or doesn't exist
        if index < 0 or index >= self.size:
            raise IndexError(f"index out of range. The index must be between 0 and {self.size}")

        #case 2: add the head
        elif index == 0:
            self.add_head(data)

        # case 3: add the tail
        elif index == self.size - 1:
            self.add_tail(data)

        # case 4:
        # principle: find the node at the position (index - 1) and this node will bethe previous node of the node to add,
        # than the node to add we have the indicated position (index)
        else:
            node = self.head
            i = 0
            # we go to the indicated position (position)
            while i < (index - 1):
                node = node.next
                i += 1
            #we create and introduce the new_node
            new_node = Node(data)
            new_node.next = node.next
            node.next = new_node
            self.size += 1 # increment the size of the list



    ############ helpers ##############

    ## get info about a specific node
    def get_node(self, index):
        if index < 0 or index >= self.size:
            raise IndexError(f"index out of range. The index must be between 0 and {self.size}")
        elif index == 0:
            return self.head
        elif index == self.size - 1:
            return self.tail
        else:
            node = self.head
            i = 0
            while i < index:
                node = node.next
                i += 1
            return node



    ## check if the list is empty
    def is_empty(self):
        return self.head is None


    ## get the length of the linked list
    def get_size(self):
        return self.size


    ## display the linked list
    def print_list(self):
        if self.head is None:
            print("List is empty")
        else:
            node = self.head
            while node:
                print(node.data,  end=" --> ")
                node = node.next
            print("None")


    ## display the head and the tail
    def print_head_tail(self):
        # case 1: The linked list is empty
        if self.size == 0:
            print("List is empty")
            print("Head is None and tail is None")
        # case 2: The linked list has one element
        elif self.size == 1:
            print("We have only one element in the list")
            print(f"Head is {self.head.data} and tail is {self.tail.data}")
        # case 3: The linked list has one element
        else:
            print(f"Head is {self.head.data} and tail is {self.tail.data}")


    ############ deletion ##############

    ##remove the first element of the list
    def remove_head(self):
        # case1: the linked list has no element
        if self.head is None:
            raise ValueError("List is empty")

        #case2: the linked list has one element
        if self.head == self.tail:
            self.head =None
            self.tail = None

        # case3: the linked list has many elements
        else:
            self.head = self.head.next
        # decrement the size of the list
        self.size -= 1



    ##remove the first element of the list
    def remove_tail(self):
        # case1: the linked list has no element
        if self.head is None:
            raise ValueError("List is empty")

        # case2: the linked list has one element
        if self.head == self.tail:
            self.head = self.tail = None

        # case3: the linked list has many elements
        else:
            node = self.head
            while node.next.next is not None:
                node = node.next
            node.next = None
            self.tail = node
        # decrement the size of the list
        self.size -= 1


    ## remove an element with a specific data
    def remove(self, data):
        # The list has no element
        if self.size == 0:
            raise ValueError("List is empty")

        # The list has one or many elements
        node = self.head
        previous_node = None
        while node is not None:
            if node.data == data:
                # the to remove node ist the head
                if node == self.head:
                    self.remove_head()
                # the to remove node ist the tail
                elif node == self.tail:
                    self.remove_tail()
                # the to remove node is in the middle of the list
                else:
                    previous_node.next = node.next
                    #node.next = None     # this line is optional in Python
                    self.size -= 1  # decrement the size of the list
                return # this line stop the verification after finding and deleting the node

            # if the current node is not the to remove node, we go to the next
            previous_node = node
            node = node.next
        # the data correspond to no node
        raise ValueError(f"data {data} not in list")

    ## remove an element at a specific index
    def remove_by_index(self, index):
        if index < 0 or index >= self.size:
            raise IndexError(f"index out of range. The index must be between 0 and {self.size}")
        if index == 0:
            self.remove_head()
        elif index == self.size - 1:
            self.remove_tail()
        else:
            i = 0
            node = self.head
            previous_node = None
            while i < index:
                i += 1
                previous_node = node
                node = node.next
            # we effectively remove the node in the index
            previous_node.next = node.next
            #node.next = None      # This line is optional in Python
        self.size -= 1  # decrement the size of the list






