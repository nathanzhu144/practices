# /* Nathan Zhu Sunday, July 13th, 2020  Stockton, CA.  Saw Amber today while walking.  
# *  Bought a lot of nepenthes veitchii (M) recently from Redleaf.  Excited to see them.  Also saw a surprisingly reddish pitcher
# *  on my Akazukin x Candy stripe veitchii, I bought from Native exotics recently.  Also bought another candy x candy today.
# *  Good stuff.
# *  Leetcode 1499 | hard | hard
# *  Category: Monotonic queue / priority queue
# */

import heapq
import collections


# nlogn soln
def findMaxValueOfEquation(points, k):
    """
    :type points: List[List[int]]
    :type k: int
    :rtype: int
    """
    pq = []
    ret = float('-inf')
    
    for x, y in points:
        while pq and x - pq[0][1] > k: heapq.heappop(pq)
        if pq: ret = max(-pq[0][0] + x + y, ret)
        heapq.heappush(pq, (x - y, x))
        
    return ret

# O(N) monotonic queue soln
def findMaxValueOfEquationN(points, k):
    """
    :type points: List[List[int]]
    :type k: int
    :rtype: int
    """
    q = collections.deque()   # a montonic queue from [greatest val of -x + y -> smallest val -x + y]
                                #                       [smallest x vals        -> largest x vals     ]
                                # queue has pairs like (-x + y, x) 
                                # Reasoning: If current (-x + y) is biggest val we have ever seen, we DEFINITELY
                                #            do not need to consider prev values, so can delete them. 
                                #            If current (-x + y) is smaller than some previous values, we MAY
                                #            use this particular value, as larger values of (-x + y) may be
                                #            zoned out by the distance k restriction.  This (-x + y) value is closer
                                #            and may happen to be biggest within k distance. 
        
    ret = float('-inf')       # tracks largest val
    
    for x, y in points:
        while q and x - q[0][1] > k: q.popleft()       # Removing invalid pairs which are more than k distance away
        if q: ret = max(q[0][0] + x + y, ret)          
        while q and -x + y >= q[-1][0]: q.pop()
        q.append((-x + y, x))
        
    return ret