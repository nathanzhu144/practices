# Nathan Zhu Tuesday December 31st, 2019 11:22 pm, Won like 5 stuffed anmials today at Santa Cruz boardwalk.
# Leetcode 1031 | medium | hard 
# If buy sell stock III is hard, this should be too.  The insight is no more obvious, and perhaps less obvious,
# this is basically same problem as buy sell stock II, but in buy sell stock II, you can buy and sell on the same day, I believe,


def maxSumTwoNoOverlap(A, L, M):
    """
    :type A: List[int]
    :type L: int
    :type M: int
    :rtype: int
    """
    
    def helper(A, L, M):
        left, right = [0] * len(A), [0] * len(A)
        
        # This calculates maximum subarray of size L up to and including index i of left.
        curr = 0
        for i in range(len(A)):
            curr += A[i]
            if i - L >= 0: curr -= A[i - L]
            if i - 1 >= 0: left[i] = max(left[i - 1], curr)
            else: left[i] = curr
        
        # This calculates maximum subarray of size M up to and including index i of right
        curr = 0
        for i in range(len(A) - 1, -1, -1):
            curr += A[i]
            if i + M <= len(A) - 1: curr -= A[i + M]
            if i + 1 <= len(A) - 1: right[i] = max(right[i + 1], curr)
            else: right[i] = curr
                
        # Since both subarrays include i, we do right[i + 1]
        ret = float('-inf')
        for i in range(len(left) - 1):
            ret = max(ret, left[i] + right[i+1])
            
        return ret
        
    return max(helper(A, L, M), helper(A, M, L))