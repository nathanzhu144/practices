#  Nathan Zhu 2:11 pm, Found a really nice dark room at Amex
#  Leetcode 240 | medium | seems about medium.
#  Category: Misc trick
#  The runtime is O(m + n) where m and n are sides of matrix.
# [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
#    ^ start here
# ]
#  Ex. Finding 22
# [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16,  X],
#   [10, 13,  X,  X,  X],
#   [X , X ,  X, 26, 30]
#    ^ start here
# ]

# Observations: Increasing left to right
#               Increasing top to bottom
#
#               Right top part is "largest" top part.
#               WE aren't guaranteed that an arbitrary element in right is bigger than arb element in left column
#
def search_2d_matrix_II(matrix, target):
    def valid(matrix, row, col):
        return not (row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]))

    if not matrix: return False
    row = len(matrix) - 1
    col = 0

    while True:
        # we walked off board, not found element
        if not valid(matrix, row, col): return False
        # we have found the target, return true
        elif matrix[row][col] == target: return True
        # go right cannot be in this column, as we are comparing against biggest item in this col
        elif matrix[row][col] < target:
            col += 1
        # go up
        elif matrix[row][col] > target:
            row -= 1




