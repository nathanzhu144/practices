## Nathan Zhu 2:39 pm, 
#  How to clone a single LL with a next and a random pointer?
#
#  There is an easy soln with a hash table O(n) space and O(n) time
#  Similar questions: See how to copy a graph
#  

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
def copyRandomList(self, head):
    """
    :type head: Node
    :rtype: Node
    """
    table = {}
    curr = head
    if head is None:
        return None
    #step 1, make hash table associations
    while curr is not None:
        table[curr] = Node(curr.val, None, None)
        curr = curr.next
        
    curr = head
    
    #use hash table associations
    while curr is not None:
        if curr.next in table:
            table[curr].next = table[curr.next]
        else:
            table[curr].next = None
            
        if curr.random in table:
            table[curr].random = table[curr.random]
        else:
            table[curr].random = None
        curr = curr.next
        
    return table[head]