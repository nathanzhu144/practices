# Nathan Zhu, 12/9/2021, 2:17 am, Stockton, CA.
# Leetcode 2074 | medium | fun!
# Category: Linked list

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverseEvenLengthGroups(head):
    """
    :type head: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    
    # prevsection -> A -> B -> C -> D -> nextsection
    #                ^              ^
    #       find count: is it N - 1?  and is it even.
    #       If even, reverse, else do nothing.
    # 
    # End should not be a nullptr here
    def helper(start, end):
        prev, curr = None, start
        
        while prev != end:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
    def reverse_k(node, ct):
        # No reversal for nullptr
        if not node: return None
        
        can_reverse_ct = 0
        start, end = node, node
        
        # We need to count how many nodes we can reverse
        # in this group because last group may have fwer than
        # ct nodes
        for i in range(ct - 1):
            if not node: break
            end = node
            node = node.next
            can_reverse_ct += 1
            
        if node: 
            can_reverse_ct += 1
            end = node
        
        next_group = end.next
        if can_reverse_ct % 2 == 0:
            helper(start, end)
            start.next = reverse_k(next_group, ct + 1)
            return end
        else:
            end.next = reverse_k(next_group, ct + 1)
            return start
        
    return None if not head else reverse_k(head, 1)
            
                
                
                
                