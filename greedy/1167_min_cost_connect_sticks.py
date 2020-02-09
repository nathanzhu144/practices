# Nathan Zhu Friday 9:57 pm Jan 17th, 2020 
# Leetcode 1167 | medium | easy
# Category: greedy
#

# You have some sticks with positive integer lengths.
# You can connect any two sticks of lengths X and Y into one stick by paying a cost of X + Y.  You perform this action until there is one stick remaining.
# Return the minimum cost of connecting all the given sticks into one stick in this way.

# Idea: Greed is good!
# 
def connectSticks(sticks):
    """
    :type sticks: List[int]
    :rtype: int
    """
    heapq.heapify(sticks)
    ret = 0
    while len(sticks) > 1:
        two = heapq.heappop(sticks) + heapq.heappop(sticks)
        ret += two
        heapq.heappush(sticks, two)
        
    return ret

