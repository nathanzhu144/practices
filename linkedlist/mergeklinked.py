# Nathan Zhu, Amex Tower, 36th Floor executive suit 5:33 pm
# Saturday June 22nd
#
# The idea for this one is divide and conquer.  This is the easiest, but probably worst approach.
# We first merge 2 linked lists in front of a queue, and then push them to the back of a queue.
# 
# What's the time complexity analysis of this one?

imports collections


def mergeKLists(lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    def merge_two(node1, node2):
        if not node1 or not node2: return node1 if node1 else node2
        if node1.val < node2.val:
            node1.next = merge_two(node1.next, node2)
            return node1
        else:
            node2.next = merge_two(node1, node2.next)
            return node2

    if not lists: return None

    lists_deq = collections.deque(lists)
    while len(lists_deq) != 1:
        temp = merge_two(lists_deq[0], lists_deq[1])
        lists_deq.popleft()
        lists_deq.popleft()
        lists_deq.append(temp)

    return lists_deq[0]

