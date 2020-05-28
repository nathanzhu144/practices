# Nathan Zhu May 21st, 2020.  
# Leetcode 430 | medium | medium
# Category: Linked list
# This one is harder than some linked list questions
# Did this one iteratively before, now recursively.

def flatten(head):
    """
    :type head: Node
    :rtype: Node
    """
    # The order of the if statement is super important.
    # 1. suppose we don't check head.child before "not head.next", there is
    #    the case where the last node has a child, but is not flattened.
    #
    # 2. The way the recursion works is we are trying to return the "last node at the end
    #    of the chain."  Therefore, we only return the node when head.next is None.
    #    Furthermore, when we call helper, we cannot do "return helper(head)", as it will
    #    return last node of linked list.
    def helper(head):
        if not head: return None
        if head.child:
            nextptr = head.next
            head.next = head.child
            head.child.prev = head
            head.child = None
            
            childend = helper(head.next)
            childend.next = nextptr
            if nextptr: nextptr.prev = childend
            
        if not head.next: return head
        return helper(head.next)
    
    node = head
    helper(node)
    return head