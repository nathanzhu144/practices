# Nathan Zhu, 12/5/2021, 4:57 pm PST, Stockton, CA
# Got a few offers recently inc SF and BBG.  
# Good time to start a new leetcode campaign.
# Leetcode 2095 | medium | makes sense
# Category: Linked list

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def deleteMiddle(self, head):
    """
    :type head: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    # Edge cases:
    # Odd number of nodes
    # Even number of nodes (2nd mid)
    # One node, dummyhead takes care of it
    # If C++, we need to delete node to prevent memory leak
    #
    # Intuition:
    # Fast and slow pointer, fast pointer moves 2x as fast, and walks off end as
    # slow reaches mid.  
    dummyhead = ListNode(0)
    dummyhead.next = head
    
    slow, prevslow, fast = head, dummyhead, head
    
    while fast.next and fast.next.next:
        fast = fast.next.next
        prevslow = slow
        slow = slow.next
    
    # slow is mid at this point, but left mid  if even number of nodes
    # but, we know there are an even number of nodes if fast.next != None
    # and fast.next.next == None
    if fast.next:
        prevslow = slow
        slow = slow.next
    prevslow.next = slow.next
    return dummyhead.next