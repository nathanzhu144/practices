# Nathan Zhu Monday July 27th, 2020 6:31 am, Stockton CA.  GOT POSITION #36/14309 for top 0.25% in Weely Contest 199.
#                                                          Last 2 weeks of SF internship.  :O  
# Leetcode 1284 | hard | hard to write clean code
# Category: BFS
# Runtime: 2^(M * N)
# 
# To make this question clean, we map a 2d board to a 1d bit array, and represent this 
# bit array as an int.  
# Then, do BFS, with the transformation function looking like bitwise operations in a small
# cross area.

import collections
    #     [0  1  0]   R = 2, C = 3
    #     [1  0  1]
    #     1 0 1 0 1 0
    
    # (C * row) + col
    # (3 * 0) + 0 = 0
    # (3 * 0) + 1 = 1
    # (3 * 0) + 2 = 2
    # (3 * 1) + 0 = 3
    # (3 * 1) + 1 = 4
    # (3 * 2) + 2 = 5
    
def minFlips(self, mat):
    """
    :type mat: List[List[int]]
    :rtype: int
    """
    if not mat or not mat[0]: return 0
    R, C = len(mat), len(mat[0])
    
    start = sum(cell << (C * r + c) for r, row in enumerate(mat) for c, cell in enumerate(row))
    
    q = collections.deque([start])
    ret = 0
    visited = set([start])
    
    while q:
        currlen = len(q)
        for i in range(currlen):
            curr = q.popleft()
            if curr == 0: return ret
            
            for r in range(R):
                for c in range(C):
                    newmove = curr
                    for dr, dc in (0, 0), (-1, 0), (1, 0), (0, 1), (0, -1):
                        newr, newc = r + dr, c + dc
                        if newr < 0 or newr >= R or newc < 0 or newc >= C: continue
                        newmove ^= (1 << (C * newr + newc))
                    if newmove in visited: continue
                    visited.add(newmove)
                    q.append(newmove)
        ret += 1
    return -1