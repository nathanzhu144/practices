# Nathan Zhu 12:30 am pm Amex Tower 36th floor, Sunday July 8thth, 2019
# Just sent Renying to airport a few hours ago, got back to Amex tower.
# Leetcode 328 | medium | not too bad

# We group all odds first, then group all evens.
# Then, we link the two.
#
def oddEvenList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    # We have a dummy for both even and odd index nodes
    odd_dummy_head = odd = ListNode(0)
    even_dummy_head = even = ListNode(0)

    while head:
        odd.next = head
        even.next = head.next
        odd = odd.next
        even = even.next

        # increment iff even is valid
        head = head.next.next if even else None

    odd.next = even_dummy_head.next
    return odd_dummy_head.next
    
