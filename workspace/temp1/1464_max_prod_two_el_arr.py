# Nathan Zhu, May 30th, 2020, Stockton, CA, during morning lc contest
# Leetcode 1464 | easy | easy
# Category: fizzbuzz


def maxProduct(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    first, sec = 0, 0
    for num in nums:
        if num > first:
            sec = first
            first = num
        elif num > sec:
            sec = num
            
    return (first - 1) * (sec - 1)