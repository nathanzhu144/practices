# Nathan Zhu Ugli 3rd floor, Jan 25th, 2020 11:25 am reading room 
# Leetcode 23 | hard | EZ
# Category: divide and conq, pq
# Runtime Nlogk.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

import heapq

def mergeKLists(lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    if not lists: return None
    head = ListNode(0)
    curr = head
    pq = []
    for node in lists:
        if node: heapq.heappush(pq, (node.val, node))
        
    while pq:
        val, node = heapq.heappop(pq)
        if node.next: heapq.heappush(pq, (node.next.val, node.next))
        
        curr.next = node
        node.next = None      
        curr = curr.next
        
    return head.next