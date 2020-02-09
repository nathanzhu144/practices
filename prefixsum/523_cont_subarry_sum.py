# Nathan Zhu Jan 26th, 2020 9:43 am Shapiro library 3rd floor
# Leetcode 523 | medium | kinda hard tbh
# Category: Prefix sum.

# Intuition:
#  [23]          23 % 6 == 5
#  [23, 2, 4]    (23 + 2 + 4) % 6 == 23 % 6, meaning we have a subarray summing up to a multiple of 6
#
# 
# Edge cases:
# 1. What if k is 0?
#    presum % 0 is undefined, but notice we want to find a continuous subarray that sums up to a multiple of k.
#    We can just at presums in this case, as we are looking for a subarray sum equal to 0.
# 2. What's with table[0] = -1?
#    We don't want to return true if the first element is a multiple of k, but we do want to return true if 
#    there is a subarray starting at 0th element that is a multiple of k.
# 
#    
#  NOTE: we ONLY add to table if the key is not present.  We always want the earliest occurrence of that mod.
# 
# 
def checkSubarraySum(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    
    
    table = dict()
    table[0] = -1   # This is important because suppose the first number is a multiple of k...and
    presum = 0
    
    for i, num in enumerate(nums):
        presum += num
        
        modded = presum
        if k != 0: modded = presum % k
        if modded in table:
            if i - table[modded] >= 2: return True   # NOT >= 1
        else: table[modded] = i
            
    return False
    
        