# Nathan Zhu Dec 1st, 2019 11:37 pm, Foundry Lofts, Flatten multilevel DLL 
# Leetcode 341 | medium | EZZZ
# Category: Linked list
# Runtime O(N^2) worst case?
# 
# Easy, just draw a diagram.


def flatten(head):
    """
    :type head: Node
    :rtype: Node
    """
    curr = head
    while curr:
        # If we have a child, we flatten.
        if curr.child:
            child = curr.child
            next_tail = child
            
            # Find tail of child layer, and connect it with curr's next (if it exists)
            while next_tail.next:
                next_tail = next_tail.next
            next_tail.next = curr.next
            if curr.next: curr.next.prev = next_tail
            
            # Makes child curr's next, and reverse.
            curr.next = child
            child.prev = curr

            # Curr has no child anymore
            curr.child = None
        
        # Move to next node
        curr = curr.next
    return head