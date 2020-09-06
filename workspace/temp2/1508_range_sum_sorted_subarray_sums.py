# /* Nathan Zhu  Saturday July 11th, 2020 Stockton, CA, Weekly contest
# *  Leetcode 1508 | medium | medium
# *  Category: presum
# */

def rangeSum(nums, n, left, right):
    """
    :type nums: List[int]
    :type n: int
    :type left: int
    :type right: int
    :rtype: int
    """
    
    N, MOD = len(nums), 10 ** 9 + 7
    presums = nums[:]
    for i in range(1, N):
        presums[i] += presums[i - 1]
        
    sums = []
    for i in range(0, N):
        for j in range(i, N):
            small = 0 if i == 0 else presums[i - 1]
            large = presums[j]
            sums.append(large - small)
            
    sums.sort()
    ret = 0
    
    for i in range(left - 1, right):
        ret += sums[i]
        ret %= MOD
        
    return ret