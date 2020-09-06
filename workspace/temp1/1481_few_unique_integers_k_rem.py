
# /* Nathan Zhu June 14th, 2020  
# *  Leetcode 1481 | medium | easy
# *  Category: priority queue
# */

import collections
import heapq
def findLeastNumOfUniqueInts(arr, n):
    """
    :type arr: List[int]
    :type k: int
    :rtype: int
    """
    c = collections.Counter(arr)
    pq = []
    for k, v in c.items():
        heapq.heappush(pq, v)
        
    while n > 0 and pq:
        count = heapq.heappop(pq)
        n -= count
        if n < 0: heapq.heappush(pq, (0, 0))
            
    return len(pq)