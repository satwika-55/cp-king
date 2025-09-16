def insert_at_beginning(self, data):
    new_node = Node(data)
    if self.head:
        new_node.next = self.head
        self.head.prev = new_node
    self.head = new_node

def delete_node(self, key):
    temp = self.head

    # If list is empty
    if not temp:
        return

    # If head needs to be deleted
    if temp.data == key:
        self.head = temp.next
        if self.head:
            self.head.prev = None
        temp = None
        return

    # Otherwise search
    while temp and temp.data != key:
        temp = temp.next

    if not temp:
        return  # not found

    if temp.next:
        temp.next.prev = temp.prev
    if temp.prev:
        temp.prev.next = temp.next

    temp = None
