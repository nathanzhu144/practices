# Nathan Zhu, Stockton, CA. May 20th, 2020. 10:43 pm.  Called Michael today for an hour.  He said he is missing 3 spoons.
# Leetcode 1462 | medium | kinda hard
# Category: Floyd-warshall transitive closure
# 

def checkIfPrerequisite(N, prereqs, queries):
    """
    :type n: int
    :type prerequisites: List[List[int]]
    :type queries: List[List[int]]
    :rtype: List[bool]
    """
    
    matrix = [[0 for c in range(N)] for r in range(N)]
    for a, b in prereqs:
        matrix[a][b] = 1
        
    for k in range(N):
        for i in range(N):
            for j in range(N):
                matrix[i][j] = matrix[i][j] or (matrix[i][k] and matrix[k][j])
                
    return [True if matrix[a][b] else False for a, b in queries]
                