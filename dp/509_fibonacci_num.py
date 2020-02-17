# Nathan Zhu Feb 10th, 2020. During 481 lecture
# Leetcode 509 | easy | EZ
# Category: DP
# This is the classic dp problem, the first one.

def fib(N):
    """
    :type N: int
    :rtype: int
    """
    if N == 0 or N == 1: return N
    arr = [0] * (N + 1)
    arr[1] = 1
    
    for i in range(2, N + 1):
        arr[i] = arr[i - 1] + arr[i - 2]
        
    return arr[-1]