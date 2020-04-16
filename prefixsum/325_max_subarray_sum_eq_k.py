# Nathan Zhu Feb 7th, 2020.  Foundry Lofts, next to bed.  So, I'm surprised this question wasn't here before.
# Leetcode 325 | medium | medium
# Category: Prefix sum

def maxSubArrayLen(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    table = dict()
    table[0] = -1
    
    presum = 0
    ret = 0
    for i, num in enumerate(nums):
        presum += num
        if presum - k in table: ret = max(i - table[presum - k], ret)
        if presum not in table: table[presum] = i

            
    return ret
