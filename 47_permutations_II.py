# Nathan Zhu 9:56 pm December 25th, 2019 Christmas Day, there is a half-eaten dragonfruit near me.
# Leetcode 47 | medium | EZ
# Not too bad
# 
# This is a case of generating permutations, but not all numbers are unique, and we don't
# want to generate repeating permutations.

import collections

def permuteUnique(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    table = collections.Counter(nums)
    ret = list()
    currpath = []
    
    def helper(currpath):
        if len(currpath) == len(nums):
            ret.append(currpath[:])
            
        for c in table:
            if table[c] > 0:
                table[c] -= 1
                currpath.append(c)
                helper(currpath)
                currpath.pop()
                table[c] += 1
    
    helper(currpath)
    return ret