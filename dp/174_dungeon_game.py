#  Nathan Zhu, 8:10 pm, Sunday June 30th, 2019 on a plane from New York to Chicago.  We were queue position 20 on the runway, no we are
#  miles in the air.
#  Leetcode 174 | hard | I think hard, too
#  
#
#  So, there are 4 situations. 
#  We solve this in a look-back manner.  This is the way we solve it.
#  
#   Given a 3 x 3 board, the order of the squares we solve is like this...
#    
#    9 8 7
#    6 5 4
#    3 2 1
# 
#  1. we are at the princess.  Health is:
#             max(1, 1 - board[row][col])
#             if board[row][col] < 0, we will get the appropriate health
#             if board[row][col] >= 0, we will need a health of 1
#  2. we are at max_col
#             so, we cannot go farther right. We must go down.
#             health = max(1, board[row + 1][col] - board[row][col])
#  3. we are at max_row
#             we cannot go farther down. we must go right
#             health = max(1, board[row][col + 1] - board[row][col])
#  4. we are not at max_row or max_col
#             we can go down OR right, so choose the ones that needs less health
#             health = max(1, min())
#    
def dungeon_game(board):
    if not board: return 1

    min_health = [[0 for col in range(len(board[0]))] for row in range(len(board))]

    max_col = len(board[0]) - 1
    max_row = len(board) - 1
    for col in range(len(board[0]) - 1, -1, -1):
        for row in range(len(board) - 1, -1, -1):
            if col == max_col and row == max_row: min_health[row][col] = max(1, 1 - board[row][col])
            elif row == max_row: min_health[row][col] = max(1, min_health[row][col + 1] - board[row][col])
            elif col == max_col: min_health[row][col] = max(1, min_health[row + 1][col] - board[row][col])
            else: min_health[row][col] = max(1, min(min_health[row + 1][col], min_health[row][col + 1]) - board[row][col])

    return min_health[0][0]

if __name__ == "__main__":
    print(dungeon_game([[1, 5], [-5, -2]]))
    
