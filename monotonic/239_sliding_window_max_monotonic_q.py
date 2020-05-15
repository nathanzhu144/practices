# Nathan Zhu Saturday, April 26th, 2020, 12:18 am.  Stockton, CA 
# Leetcode 239 | medium | kinda hard - didn't see this
# Category: Monotonic queue (used), DP (not used)
# This one really deceptively looks like a sliding window problem, but it doesn't work.
#
#
# You can keep a monotonically decreasing deque.
# 
# Insight:
# 1. Going left to right, we have two situations:
#    -  number is bigger than last number
#          last number CAN NEVER be maximum, as we have a bigger number with a larger idx
#          that last number will be removed from our sliding window before this number, and is smaller
#
#    -  number is smaller / equal to last number:
#          have to keep this number because even tho it is smaller, it could "outlast" the previous number
#
#  We can order our queue from largest valu -> smallest value, a monotonically decreasing queue.
#
# 2. To ensure the idea of a sliding window, we pop from the front of the queue
#    if the largest value is too big.
# 

import collections

def maxSlidingWindow(nums, k):
    d = collections.deque([])
    ret = []

    for i, num in enumerate(nums):
        while d and num > nums[d[-1]]:
            d.pop()

        d.append(i)
        if d[0] <= i - k: d.popleft()
        if i >= k - 1: ret.append(nums[d[0]])

    return ret

if __name__ == "__main__":
    nums = [1, 3, -3, -1, -1, 5, 3, 6, 7]
    k = 3
    print(maxSlidingWindow(nums, k))