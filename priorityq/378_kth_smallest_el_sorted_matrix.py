# Nathan Zhu April 4th, 2020 3:14 pm. Paired programming with Austin
# Leetcode 378 | medium | medium
# Category: PQ
# 
# The idea is kind of similar to djiktra.  
# The optimization here is that it runs in klogk instead of (mn)log(mn)
# 

import heapq

def kthSmallest(matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    pq = [(matrix[0][0], 0, 0)]
    R, C = len(matrix), len(matrix[0])
    visited = set()
    
    curr = None
    while k:
        curr, r, c = heapq.heappop(pq)
        if (r, c) in visited: continue
        visited.add((r, c))
        
        for dr, dc in [(0, 1), (1, 0)]:
            newr, newc = dr + r, dc + c
            if 0 <= newr < R and 0 <= newc < C:
                heapq.heappush(pq, (matrix[newr][newc], newr, newc))
        k -= 1
    return curr