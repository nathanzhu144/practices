# Nathan Zhu May 14th, 2020. Talked to Stanford guy today and he told me to do more leetcode.  Good stuff.
# Leetcode 1425 | hard | yeah kind hard
# Category: DP, montonic queue
# 
# O(N) time, O(N) space

# dp[i] represents maximum subset sum ending at index i
# dp[i] = max(0, dp[i - 1], dp[i - 2], dp[i - 3] ... dp[i - k + 1], dp[i - k]) + nums[i]
# However, note we can find the maximum previous dp sum in O(1) time with a monotonic queue.
# 
import collections
def constrainedSubsetSum(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    N = len(nums)
    dp, dq = nums[:], collections.deque()
    
    for i in range(N):
        dp[i] = max(nums[i], nums[i] + dq[0][0]) if dq else nums[i]
        
        while dq and dq[0][1] <= i - k: dq.popleft()
        while dq and dq[-1][0] <= dp[i]: dq.pop()
            
        dq.append((dp[i], i))
        
    return max(dp)


# O(NK) time, O(N) space
# basic dp, without monotonic queue, I wrote this one during the contest.
def constrainedSubsetSumTLE(nums, k):
    N = len(nums)
    dp = nums[:]
    
    for i in range(N):
        for j in range(1, k + 1):
            if i - j < 0: break
            dp[i] = max(dp[i], dp[i - j] + nums[i])
            
    return max(dp)