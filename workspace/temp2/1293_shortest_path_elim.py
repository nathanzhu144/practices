# Nathan Zhu Tuesday July 28th, 2020 11:59 am, Stockton CA.  GOT POSITION #36/14309 for top 0.25% in Weely Contest 199.
#                                                          Last 2 weeks of SF internship.  :O  Met up with Katie, also Dara/Austin yesterday
#                                                          Kaushal has good hummingbird pics.
# Leetcode 1293 | hard | hard
# Category: BFS
# Runtime: M * N * K
# 

import collections

def shortestPath(grid, k):
    """
    :type grid: List[List[int]]
    :type k: int
    :rtype: int
    """

    # Invariants:
    # If something is in the Q, we CAN visit it, as in we have enough k to get there.
    # We only re-visit a node, if we can get to there with a smaller k value.

    # 3, 2 - 1 - 2 = 
    # [0, 1, 1]
    # [1, 1, 0]
    # If k >= R 
    visited = dict()
    q = [(0, 0, k)]   # row, col, k
    R, C = len(grid), len(grid[0])
    if k >= R + C - 3: return R + C - 2    # Return early if we can def take shortest path.

    ret = 0
    while q:
        newq = []
        for r, c, newk in q:
            if r == R - 1 and c == C - 1: return ret
            visited[(r, c)] = newk
            if grid[r][c] == 1: newk -= 1
            if newk < 0: continue             # ran outta ks
                
            for dr, dc in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                newr, newc = r + dr, c + dc
                # We can visit more positions if we get a larger K, at this (r, c) position.
                if 0 <= newr < R and 0 <= newc < C and ((newr, newc) not in visited or newk > visited[(newr, newc)]):
                    visited[(newr, newc)] = newk
                    if newk == 0 and grid[newr][newc] == 1: continue
                    newq.append((newr, newc, newk))
        ret += 1
        q = newq

    return -1
if __name__ == "__main__":
    print(1)