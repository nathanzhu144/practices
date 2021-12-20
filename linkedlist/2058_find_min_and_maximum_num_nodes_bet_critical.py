# Nathan Zhu, 12/18/2021, Stockton, CA.  1:52 pm.  Going to speak at Neil's wedding next week!
# Leetcode 2058 | medium | not too bad
# Category: linked list
# This can be done with one pass, but I did it with two.


def nodesBetweenCriticalPoints(head):
    """
    :type head: Optional[ListNode]
    :rtype: List[int]
    """
    first_v, second_v, third_v = None, None, None
    i, curr = 0, head
    positions = []
    
    while curr:
        third_v = second_v
        second_v = first_v
        first_v = curr.val
        
        if third_v:
            if first_v < second_v > third_v or first_v > second_v < third_v:
                positions.append(i)
                
        curr = curr.next
        i += 1
        
    ret = [float('inf'), float('-inf')]
    for a, b in zip(positions, positions[1:]):
        ret[0] = min(ret[0], b - a)
    if positions:
        ret[1] = positions[-1] - positions[0]
        
    return ret if len(positions) >= 2 else [-1, -1]