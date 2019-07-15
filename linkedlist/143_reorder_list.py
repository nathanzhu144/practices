# Nathan Zhu 11:38 pm Amex Tower 36th floor, Sunday July 7th, 2019
# Leetcode 143 | medium | somewhat hard, combination of finding middle of a linked list
#                        flipping a linked list from 1-n, and integrating two linked list
# 
# I'm really happy.  I submitted it, and got it right in 1 try (except error checking null case)
#
# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

#  Step 1
#  1 -> 2 -> 3 -> 4 -> 5
#  
#  Step 2
#  1 -> 2 -> None
#       ^ prev
#         3 -> 4 -> 5 -> None
#         ^ mid
#
#  Step 3
#  1 -> 2 -> None
#     
#         5 -> 4 -> 3 -> None
#         ^ head2
#  NOTE: We reverse at middle pointer for both even and odd size linked lists
#
#  Step 4
#  1 -> 5 -> 2 -> 4 -> 3 -> None
#

# Reversing at middle (right middle if even)

def reorder_list(node):
    # Reverses a linked list recursively
    def reverse(node):
        if not node.next:
            return node
        newhead = reverse(node.next)
        node.next.next = node
        node.next = None
        return newhead

    # Given two linked lists, node1, node2 ecursively combines them by this rule
    # If node1 or node2 runs our of nodes, tacks the rest of the nodes on.
    #  node1 = A -> B -> None
    #  node2 = C -> D -> E-> None
    #  to
    #  A -> C -> B -> D -> E -> Nonde
    def odd_even(node1, node2):
        if not node1 or not node2: return node1 if node1 else node2

        old_node1_next = node1.next
        node1.next = node2
        node2.next = odd_even(old_node1_next, node2.next)
        return node1
    
    # For edge caeses where no linked list or linked list size 1
    if not node or node.next == None: return node
    
    # mid == middle/left middle of linked list
    # prev == node before middle
    prev, mid, fast = node, node, node
    while fast and fast.next:
        prev = mid
        fast = fast.next.next
        mid = mid.next

    # cuts linked list into two halves, step 2
    prev.next = None
    # step 3, reverse right linked list
    head2 = reverse(mid)
    # step 4, recombines linked list
    return odd_even(node, head2)

