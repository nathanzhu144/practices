# Nathan Zhu April 3rd, 2020.  Foundry Lofts. 
# Leetcode 136 | easy | easy
# Category: bits

def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ret = 0
    for num in nums: ret ^= num
    return ret
