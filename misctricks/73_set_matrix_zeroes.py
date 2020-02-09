# Nathan Zhu Feb 1st, 2020.  Foundry Lofts.  Johnny came by to do old mission capt thing today.
# Leetcode 73 | medium | pretty rough man
# Cateogory: Misc tricks
    
# Trick: Use row0, col0 to store whether we need to set a row to 0s.
# Problem: 0, 0 is ambiguous, so only use 0, 0 for row, separate var for col.
# Problem: read over write, write from bottom-up.
def setZeroes(matrix):
    if not matrix or not matrix[0]: return
    R, C = len(matrix), len(matrix[0])
    
    
    # 1, 1, 0
    # 1, 0, 1
    # 1, 1, 1
    # 
    col0 = False
    
    for r in range(R):
        if matrix[r][0] == 0: col0 = True
        for c in range(1, C):
            if matrix[r][c] == 0:
                matrix[0][c] = 0
                matrix[r][0] = 0
                
    for r in range(R - 1, -1, -1):
        for c in range(C - 1, 0, -1):
            if matrix[r][0] == 0 or matrix[0][c] == 0:
                matrix[r][c] = 0
        if col0:
            matrix[r][0] = 0