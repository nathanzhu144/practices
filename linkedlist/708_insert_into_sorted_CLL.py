# Nathan Zhu Jan 16th, 2019 Duderstadt 8:24 am, right before Apple recruiting event
# Leetcode 708 | medium | IMO hard
# This is literally the hardest linked list question I've done, like if reverse-k linked is hard, this one 
# is gotta be hard to, nasty edge cases.
# Category: linked list




# A lot of notes here:
# There are 5 cases: 
#  1.  All nodes are the same
#  2.  Not all nodes are the same
#    2a Insertion is bigger than max in node
#    2b Insertion is smaller than min in node
#    2c Insertion is within the range of the node
#  3.  Insertion into empty list
#
#  Case 3: is easy.  We handle it above, and return.  
#
#  
#  Case 2:
#  Notice we can check for all the cases in 2 at the same time.  
#  We just care about 3 cases
# 
#    - pre.val <= insertval <= curr.val means we   do something like  3  ->  (newval = 4) -> 5
# 
#    - prev.val > curr.val ensures we are at the only decreasing point inside the list (which is true if
#                                                              not all of the nodes have the same value)
# 
#      At this point, pre.val is the maximum in LL, curr.val is minimum in LL
#      If insertion value is greater than any of these extremes, (smaller or bigger), we know to add the value here
#
#  
#   Case 3:
#   Is really annoying.
#   When all the values are the same, we have no idea when we have gone through the whole linked list
#   except when prev becomes head again.  At that point, we can break.  Make sure to iterate both pointers
#   once before checking this, as otherwise the while loop would terminate immediately.
#
#   We can then insert *anywhere* and still maintain the ordering.
#
#
#  Question:
#  I was thinking, if I insert a head smaller than current value, that should become the new head, but it seems to fail for one of the
#  very last test cases, not sure why.  I actually think it is a mistake on leetcode's part.
# 
#  # return n if n.val < head.val else head
# 


# Definition for a Node.
class Node(object):
    def __init__(self, val, next):
        self.val = val
        self.next = next

class Solution(object):
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        
        n = Node(insertVal, None)
        
        # create new cyclic linked list
        if not head:
            n.next = n
            return n
    
        prev = head
        curr = head.next
    
        while True:
            if prev.val <= insertVal <= curr.val or (prev.val > curr.val and (insertVal > prev.val or insertVal < curr.val)):
                break
            prev = prev.next
            curr = curr.next
            if prev == head: break        # this line HAS to be here, and curr == head won't work
            
        n.next = curr
        prev.next = n
        return head
        