# Nathan Zhu, May 30th, 2020, Stockton, CA, during morning lc contest
# Leetcode 1460 | easy | easy
# Category: Misc tricks

import collections
def canBeEqual(target, arr):
    """
    :type target: List[int]
    :type arr: List[int]
    :rtype: bool
    """
    return collections.Counter(target) == collections.Counter(arr)