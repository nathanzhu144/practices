# Nathan Zhu May 2nd, 2020. biweekly contest
# Leetcode 1431 | easy | easy
# Category: Fizzbuzz

def kidsWithCandies(candies, extraCandies):
    """
    :type candies: List[int]
    :type extraCandies: int
    :rtype: List[bool]
    """
    N = max(candies)
    
    return [N - candy <= extraCandies for candy in candies]