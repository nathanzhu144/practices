# Nathan Zhu, 12/18/2021, Stockton, CA.  1:14 pm.  Going to speak at Neil's wedding next week!
# Leetcode 2107 | medium | classic sliding window
# Category: sliding window


import collections
def shareCandies(self, arr, k):
    """
    :type arr: List[int]
    :type k: int
    :rtype: int
    """
    c = collections.Counter(arr)
    ret = float('-inf')
    N = len(arr)
    num_flavors = len(c.keys())
    l = 0
    
    for r in range(N):
        c[arr[r]] -= 1
        if c[arr[r]] == 0: num_flavors -= 1
            
        if r - l == k:
            c[arr[l]] += 1
            if c[arr[l]] == 1: num_flavors += 1
            l += 1
            
        if r - l == k - 1:
            ret = max(ret, num_flavors)
    
    return ret