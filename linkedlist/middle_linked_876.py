def middleNode(self, head):
    """                       
    :type head: ListNode
    :rtype: ListNode
    """ 
    #NOTE: In case where there are 2 middle nodes,
    #      to return left middle: slow, fast = head, head + 1
    #      to return right middle: slow, fast = head, head
    slow, fast = head, head
    
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        
    return slow