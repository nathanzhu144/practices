# Nathan Zhu Feb 9th, 2020.  Tomorrow, I will see Andrew Zhou tomorrow morning.
# Leetcode 1176 | easy | easy
# Category: fizzbuzz

def dietPlanPerformance(calories, k, lower, upper):
    """
    :type calories: List[int]
    :type k: int
    :type lower: int
    :type upper: int
    :rtype: int
    """
    # presum = 3
    #
    # [3, 2, 1]
    #     ^
    # [3, 2, 1]
    presum = sum(calories[:k - 1])
    N = len(calories)
    ret = 0
    
    for i in range(k - 1, N):
        presum += calories[i]
        if i - k >= 0: presum -= calories[i - k]
        if presum < lower: ret -= 1
        elif presum > upper: ret += 1
            
    return ret