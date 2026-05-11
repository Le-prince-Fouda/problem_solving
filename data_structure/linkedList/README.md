# Singly Linked List in Python

This project implements a singly linked list from scratch in Python. It is designed as a data structures and algorithms exercise that demonstrates pointer-style references, node traversal, insertion, deletion, and basic error handling without relying on Python's built-in list operations for the core linked list behavior.

## Project Goals

- Build a linked list using custom `Node` objects.
- Practice algorithmic thinking through manual traversal and pointer updates.
- Implement common linked list operations such as insertion, deletion, lookup, and display.
- Demonstrate clean separation between the node model, the linked list logic, and the test/demo script.

## Project Structure

```text
linkedList/
+-- linkedList.py        # LinkedList class and linked list operations
+-- node.py              # Node class used by the linked list
+-- test_linkedList.py   # Manual test/demo script
```

## Core Concepts Demonstrated

### Node Representation

The `Node` class stores:

- `data`: the value contained in the node.
- `next`: a reference to the next node in the list.

This models the basic building block of a singly linked list.

### Linked List State

The `LinkedList` class tracks:

- `head`: the first node in the list.
- `tail`: the last node in the list.
- `size`: the number of nodes currently stored.

Keeping both `head` and `tail` allows efficient insertion at the end of the list.

## Implemented Features

### Insertion

- `add_head(data)`: creates a new node and inserts it at the beginning.
- `add_node_to_head(new_node)`: inserts an existing node at the beginning.
- `add_tail(data)`: creates a new node and inserts it at the end.
- `add_node_to_tail(new_node)`: inserts an existing node at the end.
- `insert_at_position(index, data)`: inserts a new value at a specific position.

### Deletion

- `remove_head()`: removes the first node.
- `remove_tail()`: removes the last node.
- `remove(data)`: removes the first node matching a specific value.
- `remove_by_index(index)`: removes a node at a specific index.

### Helpers

- `get_node(index)`: returns information about a node at a given index.
- `is_empty()`: checks whether the list is empty.
- `get_size()`: returns the current list size.
- `print_list()`: displays all values in order.
- `print_head_tail()`: displays the current head and tail values.

## Algorithmic Complexity

| Operation | Time Complexity | Explanation |
| --- | --- | --- |
| Add at head | O(1) | Updates the head reference directly. |
| Add at tail | O(1) | Uses the stored tail reference. |
| Insert at position | O(n) | Traverses the list to find the previous node. |
| Remove head | O(1) | Updates the head reference directly. |
| Remove tail | O(n) | Traverses the list to find the node before the tail. |
| Remove by value | O(n) | Searches for the first matching value. |
| Remove by index | O(n) | Traverses the list to reach the target index. |
| Get size | O(1) | Uses the stored `size` attribute. |
| Check empty | O(1) | Checks whether `head` is `None`. |

## How to Run

From the `linkedList` directory:

```bash
python test_linkedList.py
```

The script creates a linked list, inserts values, removes values, displays the list, and prints the current head, tail, and size at different stages.

## Example Output Pattern

The demo script shows operations such as:

```text
Is empty? True
0 --> 1 --> 2 --> 3 --> 4 --> 5 --> 6 --> 7 --> 8 --> 9 --> None
Head is 0 and tail is 9
Length: 10
```

It then continues with insertions and deletions to validate the behavior of the linked list.

## Skills Highlighted

This project demonstrates:

- Object-oriented programming in Python.
- Custom data structure implementation.
- Manual reference management using `next` pointers.
- Linked list traversal.
- Edge case handling for empty lists, single-node lists, head operations, tail operations, and invalid indexes.
- Algorithmic complexity awareness.

## Future Improvements

Possible next steps for this project:

- Add automated unit tests with `pytest`.
- Implement iteration support with `__iter__`.
- Add a `__len__` method to support Python's built-in `len()`.
- Add a `__str__` or `__repr__` method for cleaner display.
- Improve consistency in returned values from `get_node`.
- Add type hints and docstrings for better maintainability.

## About

This project is part of a personal data structures and algorithms portfolio. Its purpose is to show a clear understanding of how linked lists work internally and how common operations are implemented at a low level in Python.
