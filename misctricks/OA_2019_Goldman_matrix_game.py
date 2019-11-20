# Nathan Zhu Sunday Sept 7th, 2019 5:30 pm
# Category: Recursion, minimax
#
# 
# You have two players, A and B playing a game.
# 
# 1. A makes first move, B make second move, A makes third ...
# 2. In each move the player selects a value from the matrix, and adds that value to their score.  All matrix elements in that column are now
#    banned and cannot be used.  
# 3. Both try to play optimally.

# What is the difference in their scores if they play optimally?


# Observations:
#   [[3, 7, 5, 3, 4, 5],
#    [4, 5, 2, 6, 5, 4],
#    [7, 4, 9, 7, 8, 3]]
# 
# Say we have a grid like this.  In reality, the only squares that matter on the board is the maximum value in each column
# So, we can transform it into a 1d array representing usable squares.
#
#   [7, 7, 9, 7, 8, 5]
#
# Then, player 1 picks the maximum value (9).  The value at that index is now banned.  Player 2 picks the next max value (7), that gets banned...
# Each player picks maximum non-banned value.


def matrix_game_old(moves):
    # Banned == 0 if not banned, 1 if banned.
    banned = [0] * len(moves[0])
    real_moves = [0] * len(moves[0])

    for col in range(len(moves[0])):
        temp = float('-inf')
        for row in range(len(moves)):
            temp = max(moves[row][col], temp)
        real_moves[col] = temp

    # player is which player is currently moving.
    def helper(banned, count):
        #key = tuple(banned)
        #if key in mem: return mem[key]
        ret = float("-inf")
        if count == len(banned): return 0

        maxcol, maxnum = -1, float('-inf')
        for col in range(len(moves[0])):
            # not banned
            if banned[col] == 0 and real_moves[col] > maxnum:
                maxcol = col
                maxnum = real_moves[col]

        banned[maxcol] = 1
        ret = max(ret, maxnum - helper(banned, count + 1))
        return ret

    return helper(banned, 0)
