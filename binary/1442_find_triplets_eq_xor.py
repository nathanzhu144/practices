# Nathan Zhu, May 10th, 2020.  Contest.
# Leetcode 1442 | medium | dang I Was strugging on this one
# Category: bits
# Insight is that a subarray with an xor of 0, has at least 2 subarrays of equal xor.
# We can use a left, right prefix xor array to find this in O(N) time, for a N^2 soln.

def countTriplets(self, arr):
    """
    :type arr: List[int]
    :rtype: int
    """
    N = len(arr)
    ret = 0
    for j in range(1, N):
        for i in range(j):
            curr = 0
            for k in range(i, j + 1):
                curr ^= arr[k]
            if curr != 0: continue
            length = j - i + 1
            L_to_R, R_to_L = arr[i: j + 1], arr[i: j + 1]
            
            for i in range(1, length):
                L_to_R[i] ^= L_to_R[i - 1]
                
            for i in range(length - 2, -1, -1):
                R_to_L[i] ^= R_to_L[i + 1]
                
            for i in range(length - 1):
                if L_to_R[i] == R_to_L[i + 1]: ret += 1
            
            
    return ret