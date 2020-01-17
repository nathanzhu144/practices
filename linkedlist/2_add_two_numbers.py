# Nathan Zhu Jan 9th, 2019, 2:35 pm, probably during 376 lecture
# Leetcode 2 | medium | EZ
# Category: linked list
# Thought this was hard when I first did leetcode, now EZ.
# 


def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    falsehead = ListNode(0)
    curr = falsehead
    
    n1, n2 = l1, l2
    carry = 0
    while n1 or n2:
        val1, val2 = 0, 0
        if n1: 
            val1 = n1.val
            n1 = n1.next
        if n2:
            val2 = n2.val
            n2 = n2.next
            
        tot = val1 + val2 + carry
        newnode = ListNode(tot % 10)
        carry = tot // 10
        curr.next = newnode
        curr = curr.next
        
    if carry: curr.next = ListNode(1)
        
    return falsehead.next