# Nathan Zhu 12:07 am, Christmas Day
# Note, I could've done this problem more efficiently with a BFS.
# Similar ideas...

def orangesRotting(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    def rot(grid):
        R, C = len(grid), len(grid[0])
        newrot = 0

        for row in range(R):
            for col in range(C):
                if grid[row][col] == 2:
                    for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                        newr, newc = dr + row, dc + col
                        if 0 <= newr and newr < R and 0 <= newc and newc < C and grid[newr][newc] == 1:
                            grid[newr][newc] = 3
                            newrot += 1

        return newrot

    if not grid: return 0
    R, C = len(grid), len(grid[0])
    ret = 0

    # Count total fresh oranges
    numfresh = 0
    for row in range(R):
        for col in range(C):
            if grid[row][col] == 1: numfresh += 1
                
    # while there are fresh oranges, we rot them
    while numfresh > 0:
        newrot = rot(grid)
        
        # We write new rotten oranges as 3, to avoid RAW problems
        for row in range(R):
            for col in range(C):
                if grid[row][col] == 3: grid[row][col] = 2
        numfresh -= newrot
        ret += 1
        # If no new rotten oranges, we cannot rot all of them
        if newrot == 0 and numfresh > 0: return -1
    return ret

if __name__ == "__main__":
    orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]])