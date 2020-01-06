# Nathan Zhu 1:16 am Sunday December 29th, 2019 
# Leetcode 1254 | medium | medium
# 
# 2 ways to do this:
# 1. flood fill all islands at border, then just do number islands
# 2. modify recursive subcall to check if an island is also a closed island when flood filling
# I do #2.



def closedIsland(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    if not grid: return 0
    
    def is_closed(grid, row, col):
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]): return False
        if grid[row][col] == 1: return True
        
        grid[row][col] = 1

        # DO NOT DO THIS, THIS SHORT-CIRCUITS AND DOESN'T EVAL is_closed(b)
        # if is_closed(a) returns false, making some 0s not get colored to 1s.
        # can create new closed islands in some cases. 
        #return is_closed(a) and is_closed(b) and is_closed(c) and is_closed(d)
        first = is_closed(grid, row + 1, col)
        second = is_closed(grid, row - 1, col)
        third = is_closed(grid, row, col + 1)
        fourth = is_closed(grid, row, col - 1)
        return first and second and third and fourth
    
    ret = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 0 and is_closed(grid, row, col):
                ret += 1
    
    return ret

closedIsland([[0,0,1,1,0,1,0,0,1,0],[1,1,0,1,1,0,1,1,1,0],[1,0,1,1,1,0,0,1,1,0],[0,1,1,0,0,0,0,1,0,1],[0,0,0,0,0,0,1,1,1,0],[0,1,0,1,0,1,0,1,1,1],[1,0,1,0,1,1,0,0,0,1],[1,1,1,1,1,1,0,0,0,0],[1,1,1,0,0,1,0,1,0,1],[1,1,1,0,1,1,0,1,1,0]])