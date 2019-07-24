# Nathan Zhu 7:36 am, Amex Building 36th floor overlooking Hudson River, Monday 7:37 pm
# Leetcode 560 | medium | lol this problem took me months to understand
# 

import collections

# COMMENT THIS OUT WHEN RUNNING CODE
// Sliding window -- No, contains negative number
// hashmap + preSum
/*
    1. Hashmap<sum[0,i - 1], frequency>
    2. sum[i, j] = sum[0, j] - sum[0, i - 1]    --> sum[0, i - 1] = sum[0, j] - sum[i, j]
            k           sum      hashmap-key     -->  hashmap-key  =  sum - k
    3. now, we have k and sum.  
            As long as we can find a sum[0, i - 1], we then get a valid subarray
            which is as long as we have the hashmap-key,  we then get a valid subarray
    4. Why don't map.put(sum[0, i - 1], 1) every time ?
            if all numbers are positive, this is fine
            if there exists negative number, there could be preSum frequency > 1
*/

# Soez, this works.

def subarray_sum_eq_k(nums, k):
    previous, curr_presum, ret = collections.defaultdict(lambda: 0), 0, 0
    previous[0] = 1

    for num in nums:
        curr_presum += num
        ret += previous[curr_presum - k]
        previous[curr_presum] += 1
    
    return ret

# def subarray_sum_eq_k(nums, k):
#     if not nums: return 0
    
#     # Note that we pad the prefix sum
#     # Suppose   arr = [1, 5, 3] 
#     #       indices = [0, 1, 2]
#     #
#     #  prefixsum = [0, 1, 6, 9]
#     #    indices = [0, 1, 2, 3]
#     #
#     # Suppose we want to find sum of substring(i, j), i and j inclusive.
#     #
#     #    sum(0, 0) = prefixsum[j + 1] - prefixsum[i] = prefixsum[1] - prefixsum[0] = 1 - 0 = 1
#     #    sum(2, 2) = prefixsum[j + 1] - prefixsum[i] = prefixsum[3] - prefixsum[2] = 9 - 6 = 3
#     #    sum(0, 2) = prefixsum[j + 1] - prefixsum[i] = prefxisum[3] - prefixsum[0] = 9 - 0 = 9
#     #
#     # This allows us to find ALL possible sums of an array, REGARDLESS OF NEGATIVES,
#     # in N^2 time, where N is length of arr
#     #
    
#     prefixsum = [0] * (len(nums) + 1)
#     for i in range(1, len(nums) + 1):
#         prefixsum[i] = (prefixsum[i - 1] + nums[i - 1])
    
#     ret = 0
#     # note that i and j are inclusive indices
#     for j in range(len(nums)):
#         for i in range(j + 1):
#             if prefixsum[j + 1] - prefixsum[i] == k: ret += 1
    
#     return ret