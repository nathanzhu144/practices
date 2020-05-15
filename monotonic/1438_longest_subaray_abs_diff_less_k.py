# Nathan Zhu May 2nd, 2020. Done during weekly conctest 182, placed top 400.  Amazing.
# Leetcode 1438 | medium | kinda hard tbh
# 
# I finished the first 3 questions in the contest after spending ~29 min
# This question took me another 40ish min.  
# I originally wrote a N^2 soln and from intuition reduced it to O(N)
# with a sliding window and a monotonic queue.  I was so damn proud of myself
# for this one, like so damn proud.  This contest has been prob one of the highlights
# of 2020.
#
# Also, I crushed the hard one on this one with a "genius" idea from merging 
# k-sorted linked lists.  I was so impressed.

import collections

def longestSubarray(nums, k):
    """
    :type nums: List[int]
    :type limit: int
    :rtype: int
    """
    N = len(nums)
    small, big = collections.deque(), collections.deque()
    l, r = 0, 0
    ret = 0
    
    while r < N:
        while big and nums[r] > big[-1]:
            big.pop()
        big.append(nums[r])
        while small and nums[r] < small[-1]:
            small.pop()
        small.append(nums[r])
        r += 1
        
        while big and small and big[0] - small[0] > k:
            while l < r and nums[l] != big[0] and nums[l] != small[0]:
                l += 1
            if nums[l] == big[0]: big.popleft()
            if nums[l] == small[0]: small.popleft()
            l += 1
        ret = max(r - l, ret)
    return ret