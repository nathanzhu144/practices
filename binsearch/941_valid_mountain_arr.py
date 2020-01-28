# Nathan Zhu Jan 25th, 2019 11:04 pm
# Leetcode 941 | easy | EZ
# Category: Fizzbuzz

def validMountainArray(self, A):
    """
    :type A: List[int]
    :rtype: bool
    """
    idx = 0
    inc, dec = False, False
    N = len(A)
    
    while idx < N and (idx == 0 or A[idx] > A[idx - 1]):
        if idx >= 1: inc = True
        idx += 1
        
    while idx < N and (idx == 0 or A[idx] < A[idx - 1]):
        dec = True
        idx += 1
        
    return idx == N and inc and dec
