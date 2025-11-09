class StackList:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if not self.stack:
            raise IndexError("Underflow")
        return self.stack.pop()

    def peek(self):
        if not self.stack:
            raise IndexError("Empty stack")
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0
