#
# Here we are testing the methods of the Stack class
#

from stack import Stack


def is_empty(stack):
    empty = stack.is_empty()
    if empty:
        print('The stack is empty')
    else:
        size = len(stack)
        print(f'The stack is not empty and has: {size} element(s)')


if __name__ == '__main__':
    stack = Stack()
    is_empty(stack)
    print()

    for i in range(10):
        stack.push(i)
    print(stack)

    print('top of the stack is: ', stack.peek())
    print()

    print('dropped value: ', stack.pop())
    print('current stack: ', stack)
    print()

    print('dropped value: ', stack.pop())
    print('dropped value: ', stack.pop())
    print('current size: ', len(stack))
    print('current stack: ', stack)
    print()

    print('dropped value: ', stack.pop())
    print('dropped value: ', stack.pop())
    print('current stack: ', stack)
    print()

    is_empty(stack)
    print()

    stack.clear()
    is_empty(stack)
    print()
