

def swapPairs(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    def helper(head):
        if not head or not head.next: return head
        
        temp = head.next
        head.next = helper(head.next.next)
        temp.next = head
        return temp
    return helper(head)