
# /* Nathan Zhu June 14th, 2020  
# *  Leetcode 1480 | easy | easy
# *  Category: fizzbuzz
# */


def runningSum(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    N = len(nums)
    for i in range(1, N):
        nums[i] += nums[i - 1]
    return nums