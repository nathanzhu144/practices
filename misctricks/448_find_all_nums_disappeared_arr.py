
# Nathan Zhu March 19th, 2020
# Leetcode 448 | easy | kinda hard lol
# Category: misc tricks
# This is similar to first positive number.

def findDisappearedNumbers(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    N = len(nums)
    for i in range(N):
        if nums[abs(nums[i]) - 1] > 0:
            nums[abs(nums[i]) - 1] *= -1
    #print(nums)
    
    ret = []
    for i in range(N):
        if nums[i] > 0: ret.append(abs(i + 1))
    return ret