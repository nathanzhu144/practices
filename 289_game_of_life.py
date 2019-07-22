# Nathan Zhu Monday July 22nd, 2019, 6:59 am, Overlooking the hudson river from 36th floor conf room 200 Vessey
# Leetcode 289 | medium | med
# Category: Misc
# 
# Main challenge behind this problem is how to overcome the RAW challenges behind doing an in-place operation on
# a board without extra space.
#
# Going to bed helps find bugs. I woke up and found my bug in a minute. I was missing a parens for an if statement
# board[row][col] == 1 and (num_neighbors < 2 or num_neighbors > 3).

# Question:
# Any live cell with fewer than two live neighbors dies, as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population..
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

# Intuition:
#
# The trick here is that we can do this simulation without additional space by using the bits in a number.
# So, with 2 bits, we can store 4 states:
#
#   0 1 = alive curr -> alive next
#   1 1 = alive curr -> dead next
#   0 0 = dead curr  -> dead next
#   1 0 = dead curr  -> alive next
#
#  All board pieces start out as 0, 1 or 1, 0. So, the cool thing is that by changing squares to 2 (1, 0) and 3 (1, 1),
#  we avoid the read after write hazards we would normally get by transforming a board in-place.  In the neighbor counting
#  function, we can simply look at the last bit to figure out whether it is alive this turn.
#

def gameOfLife(board):
    """
    :type board: List[List[int]]
    :rtype: None Do not return anything, modify board in-place instead.
    """
    pos = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1,-1]]
    def get_neighbors(board, row, col):
        neigh = 0
        for dx, dy in pos:
            new_row, new_col = row + dx, col + dy
            if new_row >= 0 and new_col >= 0 and new_row < len(board) and new_col < len(board[0]):
                # If the last bit is 1, that means it is alive this turn.
                if board[new_row][new_col] & 1: neigh += 1
        return neigh

    
    for row in range(len(board)):
        for col in range(len(board[0])):
            num_neighbors = get_neighbors(board, row, col)
            # We only mark squares that will change next turn
            # Goes from dead -> alive
            if board[row][col] == 0 and num_neighbors == 3:
                board[row][col] = 2
            # Alive -> dead
            elif board[row][col] == 1 and (num_neighbors < 2 or num_neighbors > 3):
                board[row][col] = 3

    # We change all marked squares.
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 2: board[row][col] = 1
            elif board[row][col] == 3: board[row][col] = 0