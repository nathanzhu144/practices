# Nathan Zhu Thursday Jan 9th, 2019
# Leetcode 238 | medium | kinda hard if you don't see it
# Category: Misc tricks

def productExceptSelf(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    ret = [1] * len(nums)
    
    # Contribute all lefts
    for i in range(1, len(nums)):
        ret[i] = ret[i - 1] * nums[i]
    
    right = 1
    for i in range(len(nums) - 1, -1, -1):
        ret[i] *= right
        right *= nums[i]
        
    return ret

#           1     2      3     4
    
#         2,3,4  1,3,4  1,2, 4  1,2,3
        
# Numbers:     2    3    4     5
# Lefts:            2  2*3 2*3*4
# Rights:  3*4*5  4*5    5      
# Let’s fill the empty with 1:

# Numbers:     2    3    4     5
# Lefts:       1    2  2*3 2*3*4
# Rights:  3*4*5  4*5    5     1