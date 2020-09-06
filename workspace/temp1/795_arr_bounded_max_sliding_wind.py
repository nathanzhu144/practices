# Nathan Zhu June 16th, 2020, Stockton, CA.  Called Mahammadou (sp?) today.  Haven't seen him in so long, a bit less than a yaer.  He's at BAC now in NY.
# Leetcode 795 | medium | medium
# Category: DP
#
# This one kinda of splits the problem up by simplifying it.  
# How many subarrays have a max less than n?  
# 
# Take all the subarrays with a max less or eq to R, and subtract all subarrays with a max less than L
#

def numSubarrayBoundedMax(self, arr, L, R):
    """
    :type A: List[int]
    :type L: int
    :type R: int
    :rtype: int
    """

    def helper(n):
        ret = curr = 0
        
        for num in arr:
            if num <= n:
                curr += 1
                ret += curr
            else: curr = 0
        return ret
    
    return helper(R) - helper(L - 1)