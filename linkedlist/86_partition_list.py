# Nathan Zhu 11:32 pm Amex Tower 36th floor, Sunday July 7th, 2019
# Leetcode 86 | medium | easy?
# We want all nodes with a val < x to be before all nodes with val < x
# and ordering should be preserved.
#
# Trick is to construct two linked lists, and then link them.
def partition(head, x):
    """
    :type head: ListNode
    :type x: int
    :rtype: ListNode
    """
    smaller = smaller_head = ListNode(0)
    bigger = bigger_head = ListNode(0)
    
    # split linked list into two halves, one with smaller < x and
    # everything else on other one
    while head:
        if head.val < x:
            smaller.next = head
            smaller = smaller.next
        else:
            bigger.next = head
            bigger = bigger.next
        head = head.next
    
    # 1. we put a nullptr after bigger
    # 2. we connect bigger and smaller
    # 3. we return the node after dummy, as that is the new head
    bigger.next = None
    smaller.next = bigger_head.next
    return smaller_head.next