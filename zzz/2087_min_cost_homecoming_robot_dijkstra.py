# Nathan Zhu 12/10/2021, 1:31 pm, Stockton, CA
# Leetcode 2087 | medium | dijkstra is not opt soln
#
# djikstra is not the efficient solutioon for this.
# Better idea here is that all shortest paths have the same
# cost because you have the move through the same rows and
# the same columns regardless.
# O(R + C) soln, where R X C matrix.
#
import heapq

def minCost(self, startPos, homePos, rowCosts, colCosts):
    homepos = (homePos[0], homePos[1])
    # all costs are positive, so we can use djikstra
    pq = [(0, startPos[0], startPos[1])]
    R, C = len(rowCosts), len(colCosts)
    visited = set()
    
    while pq:
        cost, r, c = heapq.heappop(pq)
        if (r, c) in visited: continue
        visited.add((r, c))
        
        if (r, c) == homepos: return cost
        
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            newr, newc = r + dr, c + dc
            if newr < 0 or newc < 0 or newc >= C or newr >= R or (newr, newc) in visited: continue
            heapq.heappush(pq, (cost + rowCosts[newr] if dr != 0 else cost + colCosts[newc], newr, newc))
            
    
    # shouldn't get here
    return -1