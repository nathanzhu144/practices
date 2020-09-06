# Nathan Zhu Monday July 27th, 2020 6:31 am, Stockton CA.  GOT POSITION #36/14309 for top 0.25% in Weely Contest 199.
#                                                          Last 2 weeks of SF internship.  :O  
# Leetcode 1298 | hard | def tricky
# Category: BFS
# Runtime: N^2?
# Do a greedy BFS, kind of topological sort intuition.  Grab whatever keys you can because 
# ordering shouldn't matter.
#
# Unlike a normal BFS, we keep an array representing "reached but locked" boxes,
# and if we get a key later that unlocks the box, we can then add it to the queue
#
# Queue only contains unlocked reached boxes.
# 

import collections
def maxCandies(self, status, candies, keys, containedBoxes, initial):
    """
    :type status: List[int]
    :type candies: List[int]
    :type keys: List[List[int]]
    :type containedBoxes: List[List[int]]
    :type initialBoxes: List[int]
    :rtype: int
    """
    N, ret = len(status), 0
    q = collections.deque()
    reachable_but_locked = N * [0]
    
    for box in initial:
        if status[box] == 1: q.append(box)
        else: reachable_but_locked[box] = 1
    
    # queue is of openable boxes  
    while q:
        curr = q.popleft()
        ret += candies[curr]
        
        for key in keys[curr]:
            if reachable_but_locked[key]:
                q.append(key)
                reachable_but_locked[key] = 0
            status[key] = 1
        
        for box in containedBoxes[curr]:
            if status[box] == 1:
                q.append(box)
            else:
                reachable_but_locked[box] = 1
                                
    return ret
        