# Nathan Zhu July 23rd, 2019 6:21 pm, in the office on a weekend again.
# Leetcode 529 | medium | I think not too bad
# Category: DFS
# 
# Done in real-time in a "random-set on-site interview"
# Rating was 5.23/10, beating 84% of all users.
# 
#

def updateBoard(board, click):
    """
    :type board: List[List[str]]
    :type click: List[int]
    :rtype: List[List[str]]
    """
    # Data Stuctures #
    pos = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, -1], [-1, 1], [1, -1]]
    
    # Functions #
    
    # 
    # returns true if square is in bounds of board
    def sqvalid(board, row, col):
        return row >= 0 and col >= 0 and row < len(board) and col < len(board[0])
    
    # in surrounding 8 sq, count number of mines
    def c_surr_mines(board, row, col):
        count = 0
        for drow, dcol in pos:
            newrow, newcol = drow + row, dcol + col
            if sqvalid(board, newrow, newcol) and board[newrow][newcol] == 'M':
                count += 1
        return count
        
    # if you think about it, all "E" place can be seen as an "island".
    # we recursively use DFS to mark all "E" places to "Blank", or numbered
    # depending on number of mines in surrounding 8 squares.
    def reveal(board, row, col):
        if not sqvalid(board, row, col) or board[row][col] != 'E': return
        
        numsurroundingmines = c_surr_mines(board, row, col)
        if numsurroundingmines == 0: 
            board[row][col] = 'B'
            for drow, dcol in pos:
                newrow, newcol = drow + row, dcol + col
                reveal(board, newrow, newcol)
        else: board[row][col] = str(numsurroundingmines)

    # main function that calls everything
    def helper(board, click):
        if board[click[0]][click[1]] == 'M': board[click[0]][click[1]] = 'X'
        else: reveal(board, click[0], click[1])
        return board
    
    return helper(board, click)