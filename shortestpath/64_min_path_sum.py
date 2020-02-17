# Nathan Zhu Sunday Feb 9th, 2020 5:37 pm, with Zhongfu and Julie after eating lunch.
# Leetcode 64 | medium | fun
# Category: DP / Djikstra
# 
# Did not see this with Djikstra, this is a cool soln.

import heapq
def minPathSum(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    if not grid or not grid[0]: return 0
    
    pq = [(grid[0][0], 0, 0)]
    R, C = len(grid), len(grid[0])
    visited = set()
    while pq: 
        dist, r, c = heapq.heappop(pq)
        
        if r == R - 1 and c == C - 1:
            return dist
        
        for dr, dc in [(0, 1), (1, 0)]:
            newr, newc = dr + r, dc + c
            if newr >= R or newr < 0 or newc >= C or newc < 0 or (newr, newc) in visited: continue
            visited.add((newr, newc))
            heapq.heappush(pq, (dist + grid[newr][newc], newr, newc))
            
    # shouldn't get here
    return -1