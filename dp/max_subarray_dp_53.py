#  Nathan Zhu 11:01 pm, June 27th, 2019
#  Leetcode 53 | easy | with kadane's it is a easy
#
#  Kadane's algorithm turns the prob of finding a max subarray from N^2 to O(N), space complexity is constant,
#  as we don't need to save anything except what's needed for next calculation.
#
#  The idea is:
#  
#   [-2,1,-3,4,-1,2,1,-5]
#    
#  If cumulative sum at any point is 0, we can get a bigger subarray, by not including the previous portion.
#  At every index we check to see if we have the biggest subarray.
#    


def max_subarray_dp(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums: return 0
    
    cumulative = nums[0]
    returned = nums[0]
    
    for i in range(1, len(nums)):
        cumulative = max(0, cumulative) + nums[i]
        returned = max(cumulative, returned)
            
    return returned