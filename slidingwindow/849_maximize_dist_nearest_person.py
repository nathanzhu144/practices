# Nathan Zhu Friday Jan 3rd, 2020.  5:46 pm, Google practice OA, Wes Weimer is lecture about code review.
# Leetcode 849 | easy | easy
# Category: sliding window


def maxDistToClosest(self, seats):
    """
    :type seats: List[int]
    :rtype: int
    """
    N = len(seats)
    left = [0] * len(seats)
    right = [0] * len(seats)
    
    dist = float('inf')
    for i in range(N):
        if seats[i] == 0: dist += 1
        else: dist = 0
        left[i] = dist
        
    dist = float('inf')
    for i in range(N - 1, -1, -1):
        if seats[i] == 0: dist += 1
        else: dist = 0
        right[i] = dist
    
    ret = 0
    for i in range(N):
        ret = max(min(left[i], right[i]), ret)
        
    return ret
            