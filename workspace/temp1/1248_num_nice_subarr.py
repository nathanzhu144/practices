# Nathan Zhu, Thursday, May 28th, 2020. Stockton, CA. 8:17 pm.  
# Leetcode 1248 | medium | medium
# Category: Sliding window

import collections


# I struggled on this question for a while.  I couldn't figure out a good way to 
# do the sliding window correctly. 
#
# After sliding the left window to the left (to next odd), instead of just adding 1 to total,
# we want to add one for each non-odd number in front of the left pointer.
# 
# This soln is really smart.  We always keep k + 1 items in the buffer, with the 0th element being
# the position of the rightmost k outside the left part of our sliding window.
# In the beginning, -1 is the placeholder.
def numberOfSubarrays(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    dq, ret = collections.deque([-1]), 0         # We *need* the -1 as a placeholder for base case
    for i, num in enumerate(nums):
        if num % 2: dq.append(i)
        if len(dq) > k + 1: dq.popleft()
        if len(dq) == k + 1: ret += dq[1] - dq[0]
    return ret