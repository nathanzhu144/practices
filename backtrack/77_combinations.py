# Nathan zhu April 17th, 2020. A car was smashed outside the house today, police outside.  Stockton, CA
# Leetcode 77 | medium | EZ
# Category: Backtracking
# Simple


def combine(self, n, k):
    """
    :type n: int
    :type k: int
    :rtype: List[List[int]]
    """
    ret = []
    arr = range(1, n + 1)
    
    def helper(i, k, curr):
        if len(curr) == k:
            ret.append(curr)
            return
        if i >= len(arr):
            return
        helper(i + 1, k, curr + [arr[i]])
        helper(i + 1, k, curr)
        
    helper(0, k, [])
    return ret