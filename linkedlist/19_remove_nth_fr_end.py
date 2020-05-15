# Nathan Zhu May 8th, 2020, STarting Salesforce in a week-ish.  Saw Amber today.
# Leetcode 19 | medium | not at all bad
# Category: linkedlists


def removeNthFromEnd(self, head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    dummy = ListNode(-1)
    dummy.next = head
    fast, slow = dummy, dummy
    
    # find node n + 1 from end, for 1 ahead of deletion
    # dummy -> 1 -> 2 -> 3 -> 4 -> 5 -> NULL
    #                need^    ^to delete
    for i in range(n + 1):
        fast = fast.next
    while fast:
        fast = fast.next
        slow = slow.next
    
    slow.next = slow.next.next
    return dummy.next
