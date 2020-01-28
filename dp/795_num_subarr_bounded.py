# Nathan Zhu Jan 26th, 2019 11:25 am Ugli, 3rd floor
# Leetcode 795 | medium | kinda hard?  not too bad
# Category: DP
# Runtime O(N), space O(1)

# Suppose dp[i] denotes max number of valid subarrays ending with arr[i].
# Ex. A = [2, 1, 4, 2, 3] L = 2, R = 3
#          0  1  2  3  4
# 1. If A[i] < L
#    WE can only append A[i] to a valid subarray ending with A[i - 1] to create a new
#    subarray.  Therefore, dp[i] == dp[i - 1]
# 2. If A[i] > R
#    No valid subarray ending with A[i] exists, so dp[i] = 0
# 3. L <=  A[i] <= R
#    Any subarray starting after the previous invalid number to A[i] (A[prev + 1..i], A[prev + 2 ...i] ...) 
#    is a valid subarray.  So dp[i] += i - prev
# 

def numSubarrayBoundedMax(arr, L, R):
    """
    :type A: List[int]
    :type L: int
    :type R: int
    :rtype: int
    """
    N = len(arr)
    dp, ret = 0, 0
    prev = -1
    
    for i in range(N):
        if arr[i] < L and i > 0:
            ret += dp
        if arr[i] > R:
            dp = 0
            prev = i
        if arr[i] >= L and arr[i] <= R:
            dp = i - prev
            ret += dp
    return ret
            
        
if __name__ == "__main__":
    print(numSubarrayBoundedMax([2, 1, 4, 3], 2, 3))