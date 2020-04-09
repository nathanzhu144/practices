# Nathan Zhu Thursday, March 19th, 2020 9:48 pm. Foundry Lofts
# Leetcode 53 | easy | EZ
# Category: DP, Divide and conq

# I did this with DP in O(N) time

def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ret = float('-inf')
    
    tot = 0
    for num in nums:
        if tot < 0: tot = num
        else: tot += num
        ret = max(tot, ret)
    return ret