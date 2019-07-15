easy

def hasCycle(self, head):
    """
    :type head: ListNode
    :rtype: bool
    """
    
    if not head: return False
    
    slow = head
    fast = head.next
    
    while True:
        if not fast or not fast.next: return False
        if slow == fast: return True
        slow = slow.next
        fast = fast.next.next