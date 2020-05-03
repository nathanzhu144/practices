# Nathan Zhu May 2nd, 2020, Stockton, CA Just got top 400 for 2nd time in my life in leetcode weekly contest 182, also finished 376 finl 4 days ago.
# Leetcode 959 | medium | medium?
# Category: DFS
# 
# The trick here is to re-display the graph by increasing the size by 3.  Then, you have num islands.
#
# Ex. 
# [//]
# [//]
#
# Magnified by 2, note the up-down-left-right dfs does not work.
# [ ][/][ ][/]
# [/][ ][/][ ]
# [ ][/][ ][ ]
# [/][ ][ ][ ]
# Magnified by 3, note the udlr dfs does work
#
# [ ][ ][/][ ][ ][/]
# [ ][/][ ][ ][/][ ]
# [/][ ][ ][/][ ][ ]
# [ ][ ][/][ ][ ][ ]
# [ ][/][ ][ ][ ][ ]
# [/][ ][ ][ ][ ][ ]



def regionsBySlashes(grid):
    """
    :type grid: List[str]
    :rtype: int
    """
    def dfs(grid, r, c):
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] != 0:
            return
        grid[r][c] = 1
        dfs(grid, r + 1, c)
        dfs(grid, r - 1, c)
        dfs(grid, r, c + 1)
        dfs(grid, r, c - 1)

    if not grid: return 0
    R, C = len(grid),len(grid[0])
    
    newgrid = [[0 for c in range(C * 3)] for r in range(R * 3)]
    
    widxr = 0
    r = 0
    while r < R:
        widx = 0
        c = 0
        while c < C:
            if grid[r][c] == "\\":
                newgrid[widxr][widx] = 1
                newgrid[widxr + 1][widx + 1] = 1
                newgrid[widxr + 2][widx + 2] = 1
            elif grid[r][c] == "/":
                newgrid[widxr][widx + 2] = 1
                newgrid[widxr + 1][widx + 1] = 1
                newgrid[widxr + 2][widx] = 1
            c += 1
            widx += 3
        r += 1
        widxr += 3

    ret = 0
    for r in range(R * 3):
        for c in range(C * 3):
            if newgrid[r][c] == 0:
                ret += 1
                dfs(newgrid, r, c)
                
    return ret

if __name__ == "__main__":
    print(regionsBySlashes(["\\/","/\\"]))