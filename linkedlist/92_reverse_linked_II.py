    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n: return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        # pre should point to one before m
        # note m is 1-indexed
        for i in range(m - 1):
            prev = prev.next
        
        curr = prev.next
        rev = None        # acts like a temp prev
        
        # flips between prev and next
        for i in range(n - m + 1):
            nex = curr.next
            curr.next = rev
            rev = curr
            curr = nex
        
        prev.next.next = curr
        prev.next = rev
        
        return dummy.next