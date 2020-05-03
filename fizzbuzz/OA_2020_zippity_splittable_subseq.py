# Nathan Zhu May 1st, 2020, Doing zippity OA.  Finished 376 exam 2 days ago.
# Leetcode n/a | n/a | medium
# Category: Fizzbuzz
# Question:
# Given an array, of size N, can you split it into k subseq of size N // k, such that no
# character appears more than once in a subsequence.
#
# 
import collections
# problem 2
def partitionArray(k, numbers):
    c = collections.Counter(numbers)
    N = len(numbers)

    if N % k != 0: return False
    if [val for key, val in c.items() if val > N // k]: return False
    return True

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


# Nathan Zhu May 1st, 2020, Doing zippity OA.  Finished 376 exam 2 days ago.
# Leetcode n/a | n/a | medium
# Category: Sliding window
#
# Question:
# Given a sparse 1D parking lot, where we have up to 10^14 slots, and up to 10^5 cars, we want to find 
# to cover at least k slots with a contiguous roof.  WE want the smallest roof possible that will cover k or more cars.
# 
# Basically the idea is smallest contiguous array including more than k ones, but having the array be sparse.
# 
# Solving:
# 1. I originally did O(N) to parking slots, but this timed out.
# 2. I then did O(NlogN) to array of cars, but presorting them, and then doing sliding window on the array of cars directly.
#    This did fine.
# Problem 4
def carParkingRoof(cars, k):
    arr = sorted(cars)
    N = len(arr)
    covered = 0
    ret = float('inf')
    l, r = 0, 0

    while r < N:
        covered += 1
        r += 1

        while covered >= k:
            ret = min(arr[r - 1] - arr[l] + 1, ret)
            covered -= 1
            l += 1

    return ret

# Nathan Zhu May 1st, 2020, Doing zippity OA.  Finished 376 exam 2 days ago.
# Leetcode n/a | n/a | medium
# Category: Binary search
# Question:
# Given a N X N matrix of 0s and 1s, find the edge size of largest square size.
# 
# Ex. 
# [0, 1, 1]
# [0, 1, 1]
# [0, 1, 0]
# There is a square of size 1x1, but also since there is also a 2x2 square, we return 2
#
# Solving
# 1. If there exists a square of edge length k, there exists a square of edge length k - 1. 
#    So, we can do a binary search on edge size k.

def largestArea(samples):
    N = len(samples)

    def helper(k):
        N = len(samples)
        for r in range(N):
            if r + k > N: return False
            for c in range(N):
                if c + k > N: continue
                max_R, max_C = r + k, c + k
                valid = all(all(samples[ir][ic] for ic in range(c, max_C)) for ir in range(r, max_R))
                if valid: return True

        return False

    ret = 0
    left, right = 1, N
    while left <= right:
        mid = (right - left) // 2 + left
        if helper(mid): 
            ret = mid
            left = mid + 1
        else:
            right = mid - 1

    return ret
