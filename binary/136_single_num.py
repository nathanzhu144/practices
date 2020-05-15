# Nathan Zhu April 3rd, 2020.  Foundry Lofts. 
# Nathan Zhu May 6th, 2020. COVID-19, Good day it was ate dumplings today.
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
