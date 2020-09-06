# Nathan Zhu June 3rd, 2020, Stockton, CA 1 year + 1 day since started leetcoding! can't belive one year since new york
# Leetcode 1366 | medium | medium
# Category: PQ

import collections
import heapq

def rankTeams(votes):
    """
    :type votes: List[str]
    :rtype: str
    """
    if not votes: return ""
    table = collections.defaultdict(lambda : collections.Counter())   # char -> pos -> count
    N = len(votes[0])
    
    for i in range(len(votes)):
        for j in range(N):
            table[votes[i][j]][j] += 1
    
    pq = []
    for ch in votes[0]:
        tup = []
        for i in range(N):
            tup.append(-table[ch][i])
        tup.append(ch)
        print(tup)
        heapq.heappush(pq, tuple(tup))
    
    ret = []
    while pq:
        tup = heapq.heappop(pq)
        ret.append(tup[-1])
    return "".join(ret) 