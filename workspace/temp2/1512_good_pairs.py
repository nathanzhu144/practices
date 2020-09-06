# /* Nathan Zhu  Saturday July 11th, 2020 Stockton, CA, Weekly contest
# *  Leetcode 1512 | easy | easy
# *  Category: fizzbuzz
# */


def numIdenticalPairs(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ret, N = 0, len(nums)
    
    for i in range(N):
        for j in range(i + 1, N):
            if nums[i] == nums[j]: ret += 1
                
    return ret