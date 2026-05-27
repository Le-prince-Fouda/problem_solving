# Stack Data Structure in Python

Implementation of a **stack** data structure in Python using a linked-list approach.

This project is part of my algorithm and data structure practice. It demonstrates my ability to implement a fundamental data structure from scratch, explain how it works internally, and analyze its performance using Big O notation. The stack is implemented in Python with a linked-list approach, using custom nodes instead of relying on Python’s built-in list as the main storage mechanism.

## Purpose

A stack is a linear data structure that follows the **LIFO** principle:

> Last In, First Out

The last element added to the stack is the first one removed.

This implementation avoids using Python's built-in list as the main storage mechanism. Instead, it uses custom `Node` objects linked together, which shows how stack behavior can be built manually.

## Features

- Push a new element onto the stack.
- Pop the top element from the stack.
- Peek at the top element without removing it.
- Check whether the stack is empty.
- Get the current size of the stack in constant time.
- Clear the stack.
- Display the stack from top to bottom.

## Project Structure

```text
stack/
|-- main.py
|-- stack.py
`-- README.md
```

## Files

`stack.py`

Contains the implementation of:

- `Node`: represents one element in the linked stack.
- `Stack`: provides the stack operations.

`main.py`

Contains a simple demonstration of how to create and manipulate a stack.

## Complexity Analysis

| Operation | Description | Time Complexity |
| --- | --- | --- |
| `push(data)` | Add an element to the top | O(1) |
| `pop()` | Remove and return the top element | O(1) |
| `peek()` | Return the top element without removing it | O(1) |
| `is_empty()` | Check if the stack is empty | O(1) |
| `len(stack)` | Return the stack size | O(1) |
| `clear()` | Remove all elements | O(1) |
| `repr(stack)` | Display all elements | O(n) |

## Example Usage

```python
from stack import Stack

stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

print(stack)        # 30, 20, 10
print(stack.peek()) # 30
print(stack.pop())  # 30
print(len(stack))   # 2
```

## Running the Project

From the project directory, run:

```bash
py main.py
```

Or, if `python` is available in your environment:

```bash
python main.py
```

## Sample Output

```text
The stack is empty

9, 8, 7, 6, 5, 4, 3, 2, 1, 0
top of the stack is:  9

dropped value:  9
current stack:  8, 7, 6, 5, 4, 3, 2, 1, 0
```

## Skills Demonstrated

- Object-oriented programming in Python.
- Manual implementation of a linked data structure.
- Understanding of the LIFO principle.
- Complexity analysis with Big O notation.
- Clean separation between implementation and usage example.
- Defensive programming with explicit error handling for empty-stack operations.
