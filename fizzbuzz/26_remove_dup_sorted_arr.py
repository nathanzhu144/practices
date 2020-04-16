# Nathan Zhu March 27th, 2020 4:34 am EST.   COVID-19, Foundry Lofts
# Leetcode 26 | easy | easy
# Category: Fizzbuzz
# 
def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    #           ridx
    #     wudx
    # [1 1 2 2 3]
    # [1 2 3
    if not nums: return 0
    widx, ridx = 0, 0
    lastval = nums[widx]
    N = len(nums)
    while ridx < N:
        nums[widx] = nums[ridx]
        widx += 1
        while ridx < N and nums[ridx] == lastval:
            ridx += 1
        if ridx < N: lastval = nums[ridx]
        
    return widx
            