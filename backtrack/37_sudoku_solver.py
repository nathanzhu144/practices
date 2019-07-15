
# Nathan Zhu, Saturday July 13th, 2019, 2:42 pm, Amex building, Dark conference room.
# Leetcode 37 | hard | it isn't too bad, but dealing with boards is just annoying!
# Category: backtracking
# Runtime : 9 ^ (N * N), where N is length of each side of the board.


def solveSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: Boolean, returns true if can solve board.
            Also marks board in-place.
    """
    
    # Assuming board was valid before, if we mark row, col will board still be valid?
    def validate_move(board, row, col):
        def validate_row(board, row):
            seen = set()
            for col in range(len(board[0])):
                if board[row][col] != ".":
                    if board[row][col] in seen: return False
                    seen.add(board[row][col])
            return True

        def validate_col(board, col):
            seen = set()
            for row in range(len(board)):
                if board[row][col] != ".":
                    if board[row][col] in seen: return False
                    seen.add(board[row][col])
            return True

        def validate_3x3(board, row, col):
            seen = set()
            row, col = (row // 3) * 3, (col // 3) * 3
            for r_ in range(row, row + 3):
                for c_ in range(col, col + 3):
                    if board[r_][c_] != ".":
                        if board[r_][c_] in seen: return False
                        seen.add(board[r_][c_])
            return True
        return validate_row(board, row) and validate_col(board, col) and validate_3x3(board, row, col)
    
    # Here's the core backtracking logic.
    def helper(board):
        one_to_nine = [str(i) for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]]
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                # Given the current board, we mark current position with num
                # 1. If board is valid, we recur on it with that number in that position
                # 2. If we ever come back with helper(board) returning False, this means that
                #    marking the board here with this number leads to an unsolvable configuartion,
                #    so, we mark it back "." and try other possibilities.
                if board[row][col] == ".":
                    for num in one_to_nine:
                        board[row][col] = num
                        if validate_move(board, row, col) and helper(board): return True
                        board[row][col] = "."
                    return False

        return True
    return helper(board)
    #print(board)

if __name__ == "__main__":
    print(solveSudoku([["5","3",".",".","7",".",".",".","."],
                        ["6",".",".","1","9","5",".",".","."],
                        [".","9","8",".",".",".",".","6","."],
                        ["8",".",".",".","6",".",".",".","3"],
                        ["4",".",".","8",".","3",".",".","1"],
                        ["7",".",".",".","2",".",".",".","6"],
                        [".","6",".",".",".",".","2","8","."],
                        [".",".",".","4","1","9",".",".","5"],
                        [".",".",".",".","8",".",".","7","9"]]))