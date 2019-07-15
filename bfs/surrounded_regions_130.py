# Nathan Zhu 8:31 am Amex Tower, New York, NY
# Leetcode 130 | medium | I think easy
# The idea behind this problem is we have a grid of X and O.
# O == hole
# X == solid
# If there is a hole where you cannot reach the surface, you must fill the hole

def solve(board):
    """
    :type board: List[List[str]]
    :rtype: None Do not return anything, modify board in-place instead.
    """
    # Does a search to see if we can get out of the matrix
    # MUST BE CALLED ONLY WHEN board has an "O", no bounds checking
    def can_get_out(board, row, col, visited):
        key = (row, col)
        if key in visited: return False
        visited.add(key)
        
        if (row == 0 or col == 0 or row == len(board) - 1 or col == len(board[0]) - 1) and board[row][col] == "O":
            return True
        elif board[row][col] == "X":
            return False
        else:
            return can_get_out(board, row + 1, col, visited) or can_get_out(board, row, col - 1, visited) or \
                    can_get_out(board, row - 1, col, visited) or can_get_out(board, row, col + 1, visited)
    # Fills in an empty cavity of "O" to "X" 
    def capture(board, row, col):
        if board[row][col] == "X":
            return
        if board[row][col] == "O":
            board[row][col] = "X"
            capture(board, row + 1, col)
            capture(board, row - 1, col)
            capture(board, row, col + 1)
            capture(board, row, col - 1)
            
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == "O" and not can_get_out(board, row, col, set()):
                capture(board, row, col)
if __name__ == "__main__":
    print(solve([["X","O","X"],["O","X","O"],["X","O","X"]]))