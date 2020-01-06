# Nathan Zhu January 4th, 2019 12:09 pm, kinda sick today.
# Leetcode 51 | hard | not too bad
# Category: Backtracking
# 
# This is the classic backtracking problem.

def solveNQueens(self, n):
    """
    :type n: int
    :rtype: List[List[str]]
    """
    cols = [0] * n
    board = [["." for c in range(n)] for r in range(n)]
    queen_count = n
    
    
    def valid(row, col):
        r, c = row, col
        # Checking 135 deg digaonal
        while r >= 0 and c >= 0:
            if board[r][c] == "Q": return False
            r -= 1
            c -= 1
        r, c = row, col
        # checking 45 deg diagonal
        while r >= 0 and c < n:
            if board[r][c] == "Q": return False
            r -= 1
            c += 1
        # Checking if this col is valid.
        return cols[col] == 0

    ret = []
    def helper(row, col, queen_count):
        # We have used all the queens.
        if queen_count == 0: ret.append(["".join([board[row][col] for row in range(n)]) for col in range(n)])
            
        while row < n:
            while col < n:
                if valid(row, col):
                    board[row][col] = "Q"
                    cols[col] = 1
                    helper(row + 1, 0, queen_count - 1)
                    board[row][col] = "."
                    cols[col] = 0
                col += 1
                
            row += 1
        
    helper(0, 0, queen_count)
    return ret
