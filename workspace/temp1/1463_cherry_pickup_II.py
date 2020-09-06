# Nathan Zhu, May 30th, 2020, Stockton, CA, during morning lc contest
# Leetcode 1460 | hard | ok given cherry pickup one
# Category: DP

def cherryPickup(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    table = dict()
    
    def dfs(r, c1, c2):
        key = (r, c1, c2)
        if key in table: return table[key]
        if c1 < 0 or c2 < 0 or c1 >= len(grid[0]) or c2 >= len(grid[0]): return float('-inf')
        if r == len(grid): return 0
        
        #print(r, c1, c2)
        
        inc = 0
        if c1 == c2: inc += grid[r][c1]
        else: inc += grid[r][c1] + grid[r][c2]
            
        ret = float('-inf')
        for newc1 in [c1 - 1, c1, c1 + 1]:
            for newc2 in [c2 - 1, c2, c2 + 1]:
                ret = max(ret, dfs(r + 1, newc1, newc2) + inc)
                
        table[key] = ret
        return ret
    
    return dfs(0, 0, len(grid[0]) - 1)