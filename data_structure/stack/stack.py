class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0


    # Return the number of elements in the stack in O(1).
    def __len__(self):
        return self.size


    # Display the stack content from top to bottom in O(n).
    def __repr__(self):
        items = []
        current_item = self.top
        while current_item is not None:
            items.append(str(current_item.data))
            current_item = current_item.next
        return ', '.join(items)


    # Add a new node to the top of the stack.
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1


    # Remove and return the top element in O(1).
    def pop(self):
        if self.top is None:
            raise ValueError('Stack is empty')
        pop_data = self.top.data
        self.top = self.top.next
        self.size -= 1
        return pop_data


    # Return the top element without removing it in O(1).
    def peek(self):
        if self.top is None:
            raise ValueError('Stack is empty')
        return self.top.data

    # check if the stack has elements or not
    def is_empty(self):
        return self.top is None


    # Clear the stack in O(1).
    def clear(self):
        self.top = None
        self.size = 0
