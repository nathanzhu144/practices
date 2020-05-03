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
