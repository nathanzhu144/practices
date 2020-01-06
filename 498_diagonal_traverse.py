# Nathan Zhu Christmas Day 11:43 pm
# Leetcode 498 | medium | kinda annoying, but not bad
# Category: misc tricks

# Intuition:
# Think of a cursor, and how to move the cursor around the board.  It can only go off bounds in 4 ways,
# and there are rules for how to fix each of those ways.

def findDiagonalOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    if not matrix: return []
    row, col = 0, 0
    R, C = len(matrix), len(matrix[0])
    
    moves = [(-1, 1), (1, -1)]
    midx = 0
    ret = list()
    
    for i in range(R * C):
        ret.append(matrix[row][col])
        row += moves[midx][0]
        col += moves[midx][1]
        
        if row >= R or col >= C or row < 0 or col < 0:
            if row >= R: 
                col += 2
                row = R - 1
            elif col >= C:
                row += 2
                col = C - 1
            elif row < 0: row = 0
            elif col < 0: col = 0
            midx = (midx + 1) % 2

    return ret

if __name__ == "__main__":
    print(findDiagonalOrder([[1, 2, 3],[4, 5, 6],[7,8,9]]))