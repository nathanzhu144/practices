# Nathan Zhu Jan 4th, 2020.  9:37 pm.  South Quad, had dinner with Paul earlier.
# Leetcode 694 | medium | kinda rough
# Category: Misc tricks

def numDistinctIslands(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    visited = set()
    R, C = len(grid), len(grid[0])
    def dfs(r, c, pos, relpos):
        grid[r][c] = 0
        
        for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            newr, newc = dr + r, dc + c
            if 0 <= newr < R and 0 <= newc < C and grid[newr][newc] == 1:
                newrelpos = (relpos[0] + dr, relpos[1] + dc)
                pos.append(newrelpos)
                dfs(newr, newc, pos, newrelpos)

    for r in range(R):
        for c in range(C):
            if grid[r][c] == 1:
                posit = []
                dfs(r, c, posit, (0, 0))
                visited.add(tuple(posit))
    
    return len(visited)