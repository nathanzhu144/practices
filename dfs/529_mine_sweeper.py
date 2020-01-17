# Nathan Zhu January 29th, 2019 4:19 pm Just got back from Point Lobos yesterday.  Saw big waves.
# Leetcode 529 | medium | not too bad
# Category: DFS
# The question is kinda confusing on leetcode, but you should ONLY recursively reveal squares
# if you encounter a blank square.

def updateBoard(board, click):
    """
    :type board: List[List[str]]
    :type click: List[int]
    :rtype: List[List[str]]
    """
    moves =  [(0, 1), (1, 0), (1, 1), (-1, -1), (0, -1), (-1, 0), (-1, 1), (1, -1)]
    
    # Returns true if row, col are in board
    def in_bounds(board, row, col):
        return row >= 0 and col >= 0 and row < len(board) and col < len(board[0])
    
    # Counts how many of the surrounding 8 squares are mines.
    def count(board, row, col):
        ret = 0
        for dr, dc in moves:
            newr, newc = dr + row, dc + col
            if in_bounds(board, newr, newc):
                if board[newr][newc] == 'M': ret += 1
        return ret
    
    # Reveals recursively.
    # 1. If board[row][col] is not blank, mark with count and return
    # 2. If board[row][col] is blank, mark with B, and recurse on surrounding 8 squares.
    def reveal(board, row, col):
        if not in_bounds(board, row, col) or board[row][col] != 'E': return 0
        
        ct = count(board, row, col)
        if ct > 0: board[row][col] = str(ct)
        else:
            board[row][col] = 'B'
            for dr, dc in moves:
                newr, newc = dr + row, dc + col
                reveal(board, newr, newc)
    
    r, c = click
    if board[r][c] == 'M': 
        board[r][c] = 'X'
        return board
    
    reveal(board, r, c)
    return board