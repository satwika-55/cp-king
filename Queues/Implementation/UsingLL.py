class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueLinkedList:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, x):
        node = Node(x)
        if self.rear is None:
            self.front = self.rear = node
            return
        self.rear.next = node
        self.rear = node

    def dequeue(self):
        if self.front is None:
            raise IndexError("Underflow")
        val = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return val

    def peek(self):
        if self.front is None:
            raise IndexError("Empty Queue")
        return self.front.data

    def is_empty(self):
        return self.front is None
