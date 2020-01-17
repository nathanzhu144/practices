# Nathan Zhu Wednesday 6:50 pm, December 25th, 2019 Christmas day after gift giving
# Leetcode 650 | medium | not that easy
# Category: DP
# Runtime: N^2, space O(N)
# https://leetcode.com/problems/2-keys-keyboard/discuss/105932/Java-solutions-from-naive-DP-to-optimized-DP-to-non-DP
def minSteps(n):
    """
    :type n: int
    :rtype: int
    """
    # There must exist at least 1 copy in the whole sequence.
    # Obviously.
    # We define the number of As of the LAST copy as i.
    # i is 0 <= i < n.  i cannot be n because we can take the
    # last copy off, giving us a shorter sequence.
    #
    # There are i number of As at that point, and we have
    # n - i As left.  Since i is our last copy, we know we can
    # only paste, so this requires (n - i) / i actions.  
    # 
    # In total we have 1 + (n - i) / i actions
    #                  ^       ^ 
    #                 copy    pasting some times
    # 
    # 
    # helper(i) + 1 + (n - i) / i = helper(i) + 1 + n / i - 1
    #                             = helper(i) + n / i
    #
    
    table = dict()
    
    def helper(n): 
        if n == 1: return 0
        
        ret = float('inf')
        for i in range(1, n):
            # n has to be divisible by i
            if n % i != 0: continue
            ret = min(ret, helper(i) + n / i)
            
        table[n] = ret
        return ret
    
    return helper(n)