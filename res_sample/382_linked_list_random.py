# Nathan Zhu May 9th, 2020 1:02 am Second day of work at Salesforce is tomorrow.  Or today.
# Leetocde 382 | medium | medium
# Category: Reservoir sampling, follow-up is large linked list where you don't know the size

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import random

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head
        

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        curr, choice = self.head, None
        i = 0
        while curr:
            if random.randint(0, i) == 0:
                choice = curr
            i += 1
            curr = curr.next
            
        return choice.val
 