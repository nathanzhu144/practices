# Nathan Zhu May 21st, 2020 Stockton, CA.  Finished Day 4 work work at SF!
# Leetcode 1353 | medium | dang I struggled on this one
# Category: Intervals

import heapq
def maxEvents(self, events):
    """
    :type events: List[List[int]]
    :rtype: int
    """
    events.sort()
    ret, i, day, N = 0, 0, 0, len(events)
    pq = []
    
    while i < N or pq:
        while i < N and events[i][0] <= day:
            heapq.heappush(pq, (events[i][1]))
            i += 1
        if pq:
            heapq.heappop(pq)
            ret += 1
        while pq and pq[0] == day: heapq.heappop(pq)
        day += 1
            
    return ret
    