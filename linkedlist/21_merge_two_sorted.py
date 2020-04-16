# Nathan Zhu Jan 7th, 2020.  Did this question for the first time at the Qdoba without plugs near 
# CTC / wolverine trading.  I remember not believing this worked, but it is so simple now.
# Leetcode 21 | easy | easy
# Category: linked list


def mergeTwoLists(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    def helper(l1, l2):
        if not l1: return l2
        if not l2: return l1
        
        if l1.val < l2.val:
            l1.next = helper(l1.next, l2)
            return l1
        else:
            l2.next = helper(l1, l2.next)
            return l2
    
    return helper(l1, l2)