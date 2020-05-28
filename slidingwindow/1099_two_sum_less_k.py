# Nathan Zhu, Stockton, CA.  May 21st, 2020.  Thursday at internship
# Leetcode 1099 | easy | easy
# Category: Sliding window
# Nlogn is best time unless we can bucketsort

def twoSumLessThanK(A, K):
    """
    :type A: List[int]
    :type K: int
    :rtype: int
    """
    A.sort()
    N = len(A)
    left, right = 0, N - 1
    ret = -1
    while left < right:
        tot = A[left] + A[right]
        if tot >= K: right -= 1
        else:
            ret = max(ret, tot)
            left += 1
            
    return ret