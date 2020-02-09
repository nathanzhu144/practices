# Nathan Zhu Tuesday January 21st, 2019 3:39 pm Foundry Lofts
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
    