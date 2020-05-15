# Nathan Zhu May 13th, 2020. Calling Austin rn.  Renying and I went to pick unripe cherries today!
# Leetcode 1314 | medium | not bad
# Category: prefix sum

def matrixBlockSum(self, mat, K):
    """
    :type mat: List[List[int]]
    :type K: int
    :rtype: List[List[int]]
    """
    
    R, C = len(mat), len(mat[0])
    grid = [[mat[r][c] for c in range(C)] for r in range(R)]
    
    def get_val(r, c):
        if r < 0 or c < 0 or r >= len(mat) or c >= len(mat[0]): return 0
        return grid[r][c]
    
    
    for r in range(R):
        for c in range(C):
            grid[r][c] += get_val(r - 1, c) + get_val(r, c - 1) - get_val(r - 1, c - 1)
            
    
    ret = [[0 for c in range(C)] for r in range(R)]
    for r in range(R):
        for c in range(C):
            tr, tc = max(0, r - K), max(0, c - K)
            br, bc = min(R - 1, r + K), min(C - 1, c + K)
            
            ret[r][c] = grid[br][bc]
            if(tr > 0): ret[r][c] -= grid[tr - 1][bc]
            if(tc > 0): ret[r][c] -= grid[br][tc - 1]
            if(tr > 0 and tc > 0): ret[r][c] += grid[tr - 1][tc - 1]
                
    return ret