# Nathan Zhu 12:46 am Just got back from point Lobos yesterday, done 28 leetcode problems today.  Not bad.
# Leetcode 1091 | medium | medium
# Category: BFS

# Nothing special here, but "before or right after you make a new pair to queue, you should set grid[x][y] right away."
# Kept timing out on a simple BFS soln before I did this.
def shortestPathBinaryMatrix(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    N = len(grid)
    def get_neighbors(grid, row, col):
        ret = []
        for dr, dc in [(0, 1), (0, -1), (1, 1), (1, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1)]:
            newr, newc = dr + row, dc + col
            if newr < len(grid) and newc < len(grid[0]) and newr >= 0 and newc >= 0 and grid[newr][newc] == 0:
                grid[newr][newc] = 1                     # MASSIVE SPEED IMPROVEMENTS PRUNING HERE. 
                ret.append((newr, newc))
        return ret
    
    if grid[0][0] == 1 or grid[N - 1][N - 1] == 1: return -1
    
    q = [(0, 0)]
    ret = 0
    while q:
        newq = []
        ret += 1
        for r, c in q:
            if r == N - 1 and c == N - 1: return ret
            # grid[r][c] = 1                              # JUST SETTING HERE LEADS TO TLE
            
            for n in get_neighbors(grid, r, c):
                newq.append(n)
        q = newq
        
    return -1
        
        