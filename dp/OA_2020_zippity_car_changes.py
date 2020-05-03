# Nathan Zhu May 1st, 2020, Doing zippity OA.  Finished 376 exam 2 days ago.
# Leetcode n/a | n/a | medium
# Category: DP?  I don't think greedy works?
# Runtime: O(N)
# Question:
# Given a n-length 1D array representing barriers on a road, we want to find the minimum number of 
# moves a racecar will make to get to end of the road.  The 1d array represents the a N x 3 array of barriers.
# No matter how many squares racecar moves to the right, this counts as one move, as long as it is on one row.
#
# Ex.
# arr = [2, 1, 3, 3, 1, 1]
# 
# Corresponds to:
#
# [X - -]
# [X - -]
# [- - X]
# [- - X]
# [X - -]
# [- X -]
#    ^
#   START
# In this case, we need two changes, one move left, and one move to middle.
# 
# 
# Solving:
# 1. This can be solved with a 2d DP in O(N) time.  
#     
#    if arr[r] == c: dp[r][c] = infinity               (if pos is blocked, this one is blocked too)                
#    elif dp[r - 1][c] != infinity: dp[r][c] = dp[r][c]
#    else: dp[r][c] = min(dp[r - 1][c - 2], dp[r - 1][ c - 1], dp[r - 1][c + 1], dp[r - 1][c + 2]) + 1    for all valid columns
#
#    I could probably have done it better, but this seemed to work.
# 
# Notes: We start in middle at bottom of array.
# Problem 3
def minimumMovement(obstacles):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    N = len(obstacles)
    dp = [[float('inf') for c in range(3)] for r in range(N + 1)]
    dp[0][0] = float('inf')
    dp[0][1] = 0
    dp[0][2] = float('inf')

    for i in range(1, N + 1):
        obstacles_pos = obstacles[i - 1] - 1

        for col in range(0, 3):
            if col == obstacles_pos:
                dp[i][col] = float('inf')
                continue
            if dp[i - 1][col] != float('inf'):
                dp[i][col] = dp[i - 1][col]
                continue
            for dc in [-2, -1, 0, 1, 2]:
                lastcol = dc + col
                if 0 <= lastcol < 3:
                    dp[i][col] = min(dp[i - 1][lastcol] + 1, dp[i][col])

    return min(dp[-1][0], dp[-1][1], dp[-1][2])