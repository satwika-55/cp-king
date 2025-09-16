def reverse(self):
    temp = None
    current = self.head

    # Swap next and prev for all nodes
    while current:
        temp = current.prev
        current.prev = current.next
        current.next = temp
        current = current.prev

    # After loop, temp will be at the last node
    if temp:
        self.head = temp.prev
