def nextLargerNodes(self, head):
    """
    :type head: ListNode
    :rtype: List[int]
    """
    convert = list()
    
    # convert into a list, then it is same as daily temperatures
    while head != None:
        convert.append(head.val)
        head = head.next
        
    stack = list()
    returned = []
    
    for i in range(len(convert) - 1, -1, -1):
        while stack and convert[i] >= convert[stack[-1]]:
            stack.pop()
            
        if not stack: returned.append(0)
        else: returned.append(convert[stack[-1]])
        stack.append(i)
    
    return returned[::-1]
                