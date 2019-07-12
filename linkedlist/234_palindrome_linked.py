# Nathan Zhu, Monday July 1st, 2019, 1:29 pm
# Leetcode 234 | easy | I think easy with O(n) space, medium wth O(1) space
# 
# This is the "hard" solution where I use O(1) extra space.
# NOTE: When there are even number of nodes, it is important that 
#       slow points to the RIGHT middle.
# Step 1 
# When odd number of nodes
# 1 -> 2 -> 3 -> 2 -> 1 -> None
# ^    ^    ^ 
# head prev slow
# 
# When even number of nodes
# 1 -> 2 ->  3 -> 3 -> 2 -> 1 -> None
# ^          ^    ^ 
# head      prev slow
# 
#
# Detach and reverse
# 1 -> 2 ->  3 -> None <- 1 <- 2 <- 3
#            ^pre                   ^back_half
#                
# Reverse, and reconnect after...
#

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def isPalindrome(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    # Helper function, reverses a ll and returns the head
    def reverse(curr):
        if not curr.next:
            return curr
        
        head = reverse(curr.next)
        curr.next.next = curr
        curr.next = None
        return head
    
    
    if not head: return True
    # we get the mid point of the list. if list is odd, we want to make sure we get exact midpoint
    # pre should point to one before middle, is used to re-attach the list
    # slow should end up at middle or if there are two middles, should be at right middle
    pre, slow, fast = head, head, head
    while fast and fast.next:
        pre = slow
        slow = slow.next
        fast = fast.next.next
    
    # we save a pointer to back half so we can re-attach front to back later
    front_half = head
    back_half = reverse(slow)
    back_half_head = back_half
    pre.next = None
    
    # We iterate through the two halves to see if they're the same.
    # NOTE: If a palindrome is odd-size, since back_half size will be 1 less than front_half, so no issues
    while front_half and back_half:
        if front_half.val != back_half.val:
            pre.next = reverse(back_half_head)   # Reattaching
            return False
        front_half = front_half.next
        back_half = back_half.next
        
    pre.next = reverse(back_half_head)           # Reattaching
    return True




## Helpers ##

def print_list(head):
    if not head: return
    print(head.val)
    print_list(head.next)

def make_list(vec):
    if not vec: return None
    curr = ListNode(vec[0])
    curr.next = make_list(vec[1:])
    return curr

if __name__ == "__main__":
    head = make_list([1, 2, 3, 4, 3, 2, 1])
    print(isPalindrome(head))
    print_list(head)
    head2 = make_list([1, 2, 3, 4, 4, 3, 2, 1])
    print(isPalindrome(head2))
    print_list(head2)
    