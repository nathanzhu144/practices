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