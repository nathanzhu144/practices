# /* Nathan Zhu June 27th, 2020, Weekly contest crashed this week lol
# *  Leetcode 1493 | medium | tricky
# *  Category: sliding window
#    There's a smart DP soln too, but the dp soln scales less well with removing k elements.
# */


def longestSubarray(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ret, left, right, N = 0, 0, 0, len(nums)
    outside_one_ct = nums.count(1)
    inclusive_zero_ct = 0
    
    while right < N:
        if nums[right] == 1: outside_one_ct -= 1
        else: inclusive_zero_ct += 1
            
        right += 1
        while inclusive_zero_ct > 1:
            if nums[left] == 1: outside_one_ct += 1
            else: inclusive_zero_ct -= 1
            left += 1
            
        curr = right - left
        if inclusive_zero_ct == 1: curr -= 1
        elif outside_one_ct == 0: curr -= 1
            
        ret = max(ret, curr)
        
    return ret