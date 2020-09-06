# Nathan Zhu Tuesday July 28th, 2020 8:00 am, Stockton CA.  GOT POSITION #36/14309 for top 0.25% in Weely Contest 199.
#                                                          Last 2 weeks of SF internship.  :O  Met up with Katie, also Dara/Austin yesterday
#                                                          Kaushal has good hummingbird pics.
# Leetcode 1278 | hard | not bad
# Category: DP
# Runtime: N * N * k for DP, N^3 for precalculation.
# 

import collections
def palindromePartition(s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    cost, dp = dict(), dict()
    N = len(s)
    
    # N ^ 3 loop for calculating costs for changing each palindrome.
    for en in range(N):
        for st in range(en + 1):
            start, end, changes = st, en, 0
            while start <= end:
                if s[start] != s[end]: changes += 1
                start += 1
                end -= 1
            cost[(st, en)] = changes

    # Helper function for trying all divisions   
    def helper(starti, k):
        if starti == N:
            return float('inf') if k != 0 else 0
        key = (starti, k)
        if key in dp: return dp[key]
        ret = float('inf')
        
        # starti, endi are bounds of this section inclusive
        for endi in range(starti, N):
            ret = min(ret, cost[(starti, endi)] + helper(endi + 1, k - 1))
        dp[key] = ret
        return ret
        
        
    return helper(0, k)