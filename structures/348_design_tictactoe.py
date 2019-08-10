# Nathan Zhu, Sunday August 4th, 4:27 am.  EHS 55 John Street.  My roommate just had sex very loudly and I couldn't
#                                          fall asleep, 
# Leetcode 314 | medium | medium
# Category: Fizzbuzz, boards
# Each move is in O(1) time. 
# Intuition: 
# Whenever player 1 makes a move in a row/col, we add 1 to that row/col.
# Whenever player 2 makes a move in a row/col, we subtract 1 from that row/col
# We do this for the 2 diagonals.
# If any row/col/diagonal becomes -N or N, we know a player has won.
#
class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        # Data Structures #
        # NOTE: They will always provide a valid move.
        self.rows = [0] * n  # will track the number of moves in favor of a player in each row
        self.cols = [0] * n  # will track the number of moves in favor of a player in each col
        self.downdiag = 0    # tracks moves in favor of one sloping down left to right
        self.updiag = 0      # tracks moves in favor of one sloping up left to right
        self.n = n
        

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        mark = 1
        if player == 2: mark = -1
        
        # marks the columns
        self.rows[row] += mark
        self.cols[col] += mark
        
        # Checking n in a row
        if abs(self.rows[row]) == self.n:
            return 1 if mark == 1 else 2
        # Checking n in a col
        if abs(self.cols[col]) == self.n:
            return 1 if mark == 1 else 2
        
        # marking and checking down diagonal
        if row == col:
            self.downdiag += mark
            if abs(self.downdiag) == self.n:
                return 1 if mark == 1 else 2
        
        # marking and checking up diagonal
        if self.n - 1 - row == col:
            self.updiag += mark
            if abs(self.updiag) == self.n:
                return 1 if mark == 1 else 2
        
        return 0