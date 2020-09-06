# Nathan Zhu May 29th, 2020 Stockton, CA.  Had video call with hershal and crew today.
# Leetcode 82 | medium | easy
# Category: linked list

def deleteDuplicates(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    def helper(curr):
        if not curr: return None
        if curr and curr.next and curr.val == curr.next.val:
            delval = curr.val
            while curr and curr.val == delval:
                curr = curr.next
            return helper(curr)
        else:
            curr.next = helper(curr.next)
            return curr
    return helper(head)