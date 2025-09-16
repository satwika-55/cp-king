def delete_node(self, key):
    temp = self.head
    
    # if head node itself holds the key
    if temp and temp.data == key:
        self.head = temp.next
        temp = None
        return
    
    prev = None
    while temp and temp.data != key:
        prev = temp
        temp = temp.next
    
    if not temp:
        return  # key not found
    
    prev.next = temp.next
    temp = None
