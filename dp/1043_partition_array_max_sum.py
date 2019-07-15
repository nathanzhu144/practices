# Nathan Zhu 1:54 pm, Tuesday July 9th, 2019
# Leetcode 1043 | medium | I have found hards that are easier, but
#                          after you have the insight it is easier
# Category: Dynamic programming
#
# Note: Greedy don't work.
#
# A = | 2 | 1 | 4 | 3 |
# K = 3
# dp[0] = 0
# dp[1] = max(dp[0] + 2 * 1) = 2
# dp[2] = max(dp[0] + 2 * 2, dp[1] + 1 * 1) = max(4, 3) = 4
# dp[3] = max(dp[0] + 4 * 3, dp[1] + 4 * 2, dp[2] + 4 * 1) = max(12, 10, 8) = 12
# dp[4] = max(dp[1] + 4 * 3, dp[2] + 4 * 2, dp[3] + 3 * 1) = max(14, 12, 15) = 15
# best = | 4 | 4 | 4 | 3 |
# https://zxi.mytechroad.com/blog/dynamic-programming/leetcode-1043-partition-array-for-maximum-sum/

# NOTE: Keeping i and k 1-indexed instead of 0-indexed makes the problem a 
#       lot easier.  
def partition_array_max_sum(arr, K):
    mem = [0] * (len(arr) + 1)          
    # i = 1
    for i in range(1, len(arr) + 1):
        curr_max = float('-inf')
        # Finds maximum of choosing the last 1 .. k elements.
        for k in range(1, K + 1):
            if i - k < 0: break          # bounds checking
            curr_max = max(curr_max, arr[i - k])
            mem[i] = max(mem[i - k] + curr_max * k, mem[i])
    
    return mem[-1]


            