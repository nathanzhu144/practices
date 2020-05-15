# Nathan Zhu Tuesday January 21st, 2019 3:39 pm Foundry Lofts
# Nathan Zhu Thursday May 7th, 2020. 3:31 am Stockton, CA.  Saw Amber today while walking.
# Leetcode 674 | easy | EZ
# Category: Sliding window


def findLengthOfLCIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    N = len(nums)
    curr, ret = 0, 0
    for i in range(N):
        if not i or nums[i] > nums[i - 1]:
            curr += 1
        else:
            ret = max(ret, curr)
            curr= 1
    return max(ret, curr)
    
