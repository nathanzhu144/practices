# Nathan Zhu May 2nd, 2020. Doing mock interview with george today
# Leetcode 994 | easy | easy
# Category: set BFS


def orangesRotting(grid):
    if not grid: return 0
    R, C = len(grid), len(grid[0])
    fresh, rotten = set(), set()
    
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 2: rotten.add((r, c))
            elif grid[r][c] == 1: fresh.add((r, c))
    
    minutes = 0
    while rotten and fresh:
        newrotten = set()
        
        for r, c in rotten:
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                newr, newc = r + dr, c + dc
                if (newr, newc) in fresh: newrotten.add((newr, newc))
                
        rotten = newrotten
        fresh -= newrotten
        minutes += 1
    return minutes if not fresh else -1