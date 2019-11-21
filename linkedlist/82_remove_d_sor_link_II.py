def deleteDuplicates(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    numbers = collections.defaultdict(int)
    dummy = ListNode(None)
    dummy.next = head
    
    curr = dummy
    while curr:
        numbers[curr.val] += 1
        curr = curr.next
    
    curr = dummy
    while curr and curr.next:
        if numbers[curr.next.val] >= 2:
            curr.next = curr.next.next
        else:
            curr = curr.next
        
    return dummy.next