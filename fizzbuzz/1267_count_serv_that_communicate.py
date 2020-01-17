# Nathan Zhu
# Leetcode 1267 | medium | medium
# 
#  S  S  .  .
#  .  .  .  .
#  .  .  S  .
#  .  .  S  .
#  .  .  .  [S]
# Only [S] cannot communicate with any other servers, as there is no server on same row or column.
# I do this in O(N * M) time

# You are given a map of a server center, represented as a m * n integer matrix 
#  where 1 means that on that cell there is a server and 0 means that it is no server. 
# Two servers are said to communicate if they are on the same row or on the same column.
#
# Return the number of servers that communicate with any other server.

def countServers(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    if not grid: return 0
    R, C = len(grid), len(grid[0])
    rows = R * [0]
    cols = C * [0]
    
    for row in range(R):
        for col in range(C):
            if grid[row][col] == 1:
                rows[row] += 1
                cols[col] += 1
    ret = 0
    for row in range(R):
        for col in range(C):
            if grid[row][col] == 1 and (rows[row] > 1 or cols[col] > 1): ret += 1
        return ret

countServers([[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]])

#  [[1,1,0,0]
# ,[0,0,1,0],
# [ 0,0,1,0],[
#  0,0,0,1]])