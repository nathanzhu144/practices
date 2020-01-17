# Nathan Zhu January 3rd, 2019 11:45 pm Think I'm coming down with a cold...
# Leetcode 1004 | medium | EZ
# Category: sliding window

# This is literally just a sliding window problem.
# problem
# Given an array A of 0s and 1s, we may change up to K values from 0 to 1.
# Return the length of the longest (contiguous) subarray that contains only 1s. 

def longestOnes(self, A, K):
    """
    :type A: List[int]
    :type K: int
    :rtype: int
    """
    
    left, right = 0, 0
    num_z = 0
    ret = 0
    while right < len(A):
        if A[right] == 0: num_z += 1
        right += 1
        
        while left < right and num_z > K:
            if A[left] == 0: num_z -= 1
            left += 1
            
        ret = max(ret, right - left)
        
    return ret