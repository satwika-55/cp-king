class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.top = None

    def push(self, x):
        node = Node(x)
        node.next = self.top
        self.top = node

    def pop(self):
        if not self.top:
            raise IndexError("Underflow")
        val = self.top.data
        self.top = self.top.next
        return val

    def peek(self):
        if not self.top:
            raise IndexError("Empty stack")
        return self.top.data

    def is_empty(self):
        return self.top is None
