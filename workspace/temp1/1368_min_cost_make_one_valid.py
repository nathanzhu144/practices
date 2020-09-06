# Nathan Zhu, June 3rd, 2020 Stockton, CA.  Been a year and a day since the beginning!  Old Nathan would be proud.
# Leetcode 1368 | hard | hard
# Category: BFS

def minCost(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    if not grid or not grid[0]: return 0 #invalid grid
    R, C = len(grid), len(grid[0])
    moves = dict()
    moves[1] = (0, 1)
    moves[2] = (0, -1)
    moves[3] = (1, 0)
    moves[4] = (-1, 0)
    visited = [[float('inf') for c in range(C)] for r in range(R)]
    BFS = []
    k = 0
    
    def dfs(r, c):
        if r < 0 or c < 0 or r >= R or c >= C or visited[r][c] != float('inf'): return
        BFS.append((r, c))
        visited[r][c] = k
        dfs(r + moves[grid[r][c]][0], c + moves[grid[r][c]][1])
    
    dfs(0, 0)
    while BFS:
        k += 1
        BFS, tBFS = [], BFS
        for r, c in tBFS:
            for dr, dc in moves.values():
                dfs(r + dr, c + dc)
    return visited[-1][-1]
            