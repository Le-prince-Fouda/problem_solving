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
        self.size += 1


    ## This method works in the same way as ‘add_head’, but in this case, an existing node is added as the head node.
    ## add_head create first the node than add it as the head
    def add_node_to_head(self, new_node: Node):
        new_node.next = self.head # our node is the previous node of the head of the linked list
        self.head = new_node # now the created node is the first of the linked list
        self.size += 1



    ## this methode create and add a node as the tail of the linked list
    def add_tail(self, data):
        new_node = Node(data) # we create the node to add

        # case 1: The linkedlist is empty
        if self.head is None:
            self.head = new_node
            self.tail = self.head

        # case 2: The linkedlist has one or more nodes
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1



    ## this methode add an existing node as the tail of the linked list
    def add_node_to_tail(self, new_node: Node):
        # case 1: The linkedlist is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        # case 2: The linkedlist has one or more nodes
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1


    def insert_at_position(self, index, data ):
        #case 1: negativ index
        if index < 0:
            raise IndexError("The index cannot be negative")

        #case 2: index doesn't exist
        elif index >= self.size:
            raise IndexError("The index cannot be greater than the size")

        #case 3: add the head
        elif index == 0:
            self.add_head(data)

        # case 4: add the tail
        elif index == self.size - 1:
            self.add_tail(data)

        # case 5:
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
            self.size += 1



