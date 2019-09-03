# Nathan Zhu August 26th, 2019 10:05 pm, Stockton California at buffalo wild wings
# Leetcode 445 | medium | I think not too bad
# Category: Linked list
# 
# Done in real-time in a "Microsoft OA", 1 hour time for 2 questions
# Rating was 6.06/10, beating 66% of all users.
# 


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def addTwoNumbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    # Step 1: Reverse both of the linked lists, keeping track of the head pointers
    # 
    #         We go back to front, adding the values together, we also to keep a carry value.
    #
    # Step 2: We iterate through both LL, adding each valu together.
    
    def reverse(head):
        prev = None
        curr = head

        while curr:
            nextp = curr.next
            curr.next = prev
            prev = curr
            curr = nextp
            
        return prev
    
    rl1 = reverse(l1)
    rl2 = reverse(l2)
    rl1cpy, rl2cpy = rl1, rl2
    newhead = ListNode(0)
    curr = newhead
    carry = 0

    while rl1 or rl2:
        rl1_val, rl2_val = 0, 0
        if rl1: 
            rl1_val = rl1.val
            rl1 = rl1.next
        if rl2: 
            rl2_val = rl2.val
            rl2 = rl2.next
        
        totsum = rl1_val + rl2_val + carry
        carry = totsum // 10
        curr.next = ListNode(totsum % 10)
        curr = curr.next
        
    if carry:
        curr.next = ListNode(1)
        
    return reverse(newhead.next)