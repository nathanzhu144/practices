# Nathan Zhu Wednesday 7:38 pm, December 25th, 2019 Christmas day after gift giving
# Leetcode 651 | medium | not that easy
# Category: DP
# Runtime: N^2, space O(N)

def maxA(N):
    """
    :type N: int
    :rtype: int
    """
    
    # For larger values of N, there will generally be at least
    # one ctrl-A, ctrc-C followed by some ctrl-V.  If this is true,
    # this sequence must also have a LAST ctrl-A, ctrl-C, followed by
    # at least one ctrl-V.  
    # 
    # Obviously there will be at least one ctrl-V, as we could make a longer
    # sequeence of As by taking out the ctrl-A, ctrl-C, and simply putting in two
    # As.
    #
    # Suppose that at this point, we have taken i actions, where 1 <= i < n.
    # Given that we have taken i actions, and we have n actions total, we do:
    # 
    # 1   +  1   +   (n - i - 2) 
    # ^
    # Ct-A  Ct-C      Ct-V (number of times)
    # 
    # Since we already have 1 of the As sequences, 
    # we have the recurrence relation
    # 
    # maximum As given we start at helper(i): helper(i) * (n - i - 1)
    #
    #
    #
    # Also: There exist Ns, where it is optimal to only print As.
    #       
    
    
    table = dict()
    def helper(n):
        if n in table: return table[n]
        
        # There exist Ns where it is optimal to only print As.
        ret = n
        for i in range(1, n):
            # We only care about the calculation when (n - i - 1) is positive.
            if n - i - 1 > 0:
                ret = max(ret, helper(i) * (n - i - 1))
        
        table[n] = ret
        return ret
        
    return helper(N)