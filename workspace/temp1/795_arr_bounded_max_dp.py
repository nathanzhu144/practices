# Nathan Zhu June 16th, 2020, Stockton, CA.  Called Mahammadou (sp?) today.  Haven't seen him in so long, a bit less than a yaer.  He's at BAC now in NY.
# Leetcode 795 | medium | medium
# Category: DP
#
# There's a kinda cool counting argument too with inclusion exclusion
# This DP solution is REALLY smart though
def numSubarrayBoundedMax(arr, L, R):
    """
    :type A: List[int]
    :type L: int
    :type R: int
    :rtype: int
    """
    N = len(arr)
    dp, ret = 0, 0
    prev = -1
    
    for i in range(N):
        if arr[i] < L and i > 0:
            ret += dp
        if arr[i] > R:
            dp = 0
            prev = i
        if arr[i] >= L and arr[i] <= R:
            dp = i - prev
            ret += dp
    return ret