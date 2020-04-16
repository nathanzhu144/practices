# Nathan Zhu Aprtil 2nd, 2020, Foundry Lofts.  Final week, COVID-19
# Leetcode 840 | easy | not at all easy
# Category: Fizzbuzz
# Damn this one annoying

def numMagicSquaresInside(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    def helper(r, c):
        curr = set()
        for cr in range(r, r + 3):
            for cc in range(c, c + 3):
                curr.add(str(grid[cr][cc]))
        a =  set("1 2 3 4 5 6 7 8 9".split())
        if curr != set("1 2 3 4 5 6 7 8 9".split()): return False
        
        for dr in range(3):
            if grid[dr + r][c] + grid[dr + r][c + 1] + grid[dr + r][c + 2] != 15: 
                return False
        
        for dc in range(3):
            if grid[r][dc + c] + grid[r + 1][dc + c] + grid[r + 2][dc + c] != 15: 
                return False
        if grid[r][c] + grid[r + 1][c + 1] + grid[r + 2][c + 2] != 15: return False
        if grid[r + 2][c] + grid[r + 1][c + 1] + grid[r][c + 2] != 15: return False
        return True
    
    ret = 0
    R, C = len(grid), len(grid[0])
    for r in range(R - 2): 
        for c in range(C - 2):
            if grid[r + 1][c + 1] == 5:
                if helper(r, c): ret += 1
    return ret