class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def hasCycle(head: ListNode) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:  # cycle detected
            return True
    return False


# TO FIND THE START OF THE CYCLE: 

def detectCycle(head: ListNode) -> ListNode:
    slow = fast = head
    # Step 1: Detect if cycle exists
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:  # collision
            break
    else:
        return None  # no cycle

    # Step 2: Find cycle start
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow
