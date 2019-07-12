# Nathan Zhu 11:30 pm Amex Tower 36th floor, Sunday July 7th, 2019
# Leetcode 142 | medium | not too easy
#
# Just got back form JFK - sent Renying to airport.  
# Long day, kinda tired.
# 
# I actually still don't quite understand the "trick" and why it works.  I thought about it for an 
# hour and kinda gave up.

    #    Consider the following linked list, where E is the cylce entry and X, the crossing point of fast and slow.
    #     H: distance from head to cycle entry E
    #     D: distance from E to X
    #     L: cycle length
    #                       _____
    #                      /     \
    #     head_____H______E       \
    #                     \       /
    #                      X_____/   
        
    
    #     If fast and slow both start at head, when fast catches slow, slow has traveled H+D and fast 2(H+D). 
    #     Assume fast has traveled n loops in the cycle, we have:
    #     2H + 2D = H + D + nL  -->  H + D = nL  --> H = nL - D
    #
    # 


def ll_cycle_II(node):
    slow, fast = node, node
    while fast and fast.next:
        if slow == fast:
            # If we start a pointer at head, and move it at the same rate as slow,
            # they will the point where you enter the loop of the linked list.
            slow2 = node  # slow2 starts at head
            while slow2 != slow:
                slow2 = slow2.next
                slow = slow.next
            return slow

        slow = slow.next
        fast = fast.next.next
    
    return None