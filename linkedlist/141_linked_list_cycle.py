# Nathan Zhu, April 4th, 2020, during COVID-19.  Crushed the binary search question on the 376 final.
# Leetcode 141 | easy | easy
# Category: Linked list
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
