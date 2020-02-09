# Nathan Zhu Jan 30th, 2020 Duderstadt Library  Early morning.  Doing the work, saw a turkey today.
# Leetcode 237 | easy | DUDE MAN
# Category: Linked list Brainteaster... 
# Could not figure this out.
# They tell you to delete a node, but don't give prev node.  You're supposed to assign
# the val of last node to this node, and delete next node.  Only works if not deleting last
# ptr.

def deleteNode(self, node):
    """
    :type node: ListNode
    :rtype: void Do not return anything, modify node in-place instead.
    """
    node.val = node.next.val
    node.next = node.next.next
    