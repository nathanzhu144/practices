# Nathan Zhu Feb 4th, 2020.  6:00 am Was just outside Brugel's bagels  A good day.
# Leetcode 1053 | medium | similar to next perm
# Category: misc tricks




def prevPermOpt1(A):
    """
    :type A: List[int]
    :rtype: List[int]
    """
    if not A or len(A) < 2: return A
    
    N = len(A)
    if all(A[i] <= A[i + 1] for i in range(N - 1)): return A
    
    # find first bigger one
    left = N - 2
    while A[left] <= A[left + 1]: left -= 1
        
    right = N - 1
    while A[right] >= A[left]: right -= 1
    while A[right] == A[right - 1]: right -= 1
    A[left], A[right] = A[right], A[left]
    
    return A