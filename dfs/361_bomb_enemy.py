# Nathan Zhu Jan 31st, 2020 Foundry Lofts 10:00 pm, Finishing up for the evening.
# Leetcode 361 | medium | not bad
# Category: DP / DFS
# With DP, you can I think go frm 4N^2 to N^2, but I did the non-dp way.

def maxKilledEnemies(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    if not grid or not grid[0]: return 0
    R, C = len(grid), len(grid[0])
    
    def bomb(r, c, dr, dc):
        ret = 0
        while 0 <= r < R and 0 <= c < C and grid[r][c] != "W":
            if grid[r][c] == "E": ret += 1
            r, c = dr + r, dc + c
        return ret
    
    ret = 0
    for r in range(R):
        for c in range(C):
            if grid[r][c] == "0":
                curr = bomb(r, c, 0, 1) + bomb(r, c, 0, -1) + bomb(r, c, -1, 0) + bomb(r, c, 1, 0)
                ret = max(curr, ret)
                
    return ret