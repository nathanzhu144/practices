
# Nathan Zhu, Saturday July 13th, 2019, 11:23 am, Amex building, Dark conference room.
# Leetcode 36 | medium | annoying as hell, not hard, but annoying
# Category: fizzbuzz
# Runtime : N^2


def isValidSudoku(board):
    one_to_nine = set(str(i) for i in [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def validate_row(board, row):
        seen = set()
        for col in range(len(board[0])):
            if board[row][col] != ".":
                if board[row][col] not in one_to_nine: return False
                if board[row][col] in seen: return False
                seen.add(board[row][col])
        return True
    
    def validate_col(board, col):
        seen = set()
        for row in range(len(board)):
            if board[row][col] != ".":
                if board[row][col] not in one_to_nine: return False
                if board[row][col] in seen: return False
                seen.add(board[row][col])
        return True
    
    def validate_3x3(board, row, col):
        seen = set()
        for r_ in range(row, row + 3):
            for c_ in range(col, col + 3):
                if board[r_][c_] != ".":
                    if board[r_][c_] not in one_to_nine: return False
                    if board[r_][c_] in seen: return False
                    seen.add(board[r_][c_])
        return True

    # validate row/col
    for i in range(9):
        if not validate_row(board, i): return False
        if not validate_col(board, i): return False
    
    # validate all 3x3s, really ugly code 
    r, c = 0, 0
    while r < 9:
        while c < 9:
            if not validate_3x3(board, r, c): return False
            c += 3
        c = 0
        r += 3
    return True

if __name__ == "__main__":
    print(isValidSudoku([
                        ["5","3",".",".","7",".",".",".","."],
                        ["6",".",".","1","9","5",".",".","."],
                        [".","9","8",".",".",".",".","6","."],
                        ["8",".",".",".","6",".",".",".","3"],
                        ["4",".",".","8",".","3",".",".","1"],
                        ["7",".",".",".","2",".",".",".","6"],
                        [".","6",".",".",".",".","2","8","."],
                        [".",".",".","4","1","9",".",".","5"],
                        [".",".",".",".","8",".",".","7","9"]
                        ]))