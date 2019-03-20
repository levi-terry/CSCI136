# Author: LDT
# Date: 11MAR2019
# Title: stack.py
# Description: This program implements a stack linked list along
# with functions to add to (push) and remove from (pop) the stack.

import sys


# Stack class is a linked list for first in-last out operations
class Stack:
    def __init__(self):
        self.first = None

    # Returns True if stack is empty
    def isEmpty(self):
        return self.first is None

    # Add node to top of stack, setting new first's next to the previous first (top of stack)
    def push(self, item):
        self.first = Node(item, self.first)

    # Remove top of stack by point stack's first to first's next
    def pop(self):
        self.first = self.first.next

    # Use a pointer to iterate through the stack starting from first and moving to each first.next until
    # there is no next.
    def display(self):
        ptr = self.first
        while ptr is not None:
            print(ptr.item)
            ptr = ptr.next


class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next


def main():
    stack = Stack()
    for line in sys.stdin:
        if line == '-\n':
            stack.pop()
        else:
            stack.push(line)
    stack.display()


if __name__ == '__main__':
    main()
