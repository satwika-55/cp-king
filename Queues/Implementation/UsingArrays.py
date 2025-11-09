class QueueArray:
    def __init__(self):
        self.queue = []

    def enqueue(self, x):
        self.queue.append(x)      # add to end (rear)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Underflow")
        return self.queue.pop(0)  # remove from front

    def peek(self):
        if self.is_empty():
            raise IndexError("Empty Queue")
        return self.queue[0]      # front element

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)
