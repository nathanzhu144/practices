# Nathan Zhu April 9th, 2020, Stockton, CA, 7:18 am
# Leetcode 611 | medium | medium
# Category: Sliding window


def triangleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # 2 2 3  4  6  7 
    #          fix
    # f      s
    #
    # 2 2
    # [2 2 4]
    N = len(nums)
    arr = sorted(nums)
    if N <= 2: return 0
    ret = 0
    
    for third in range(2, N):
        first, sec = 0, third - 1
        while first < sec:
            if arr[first] + arr[sec] <= arr[third]:
                first += 1
            else:
                ret += sec - first
                sec -= 1
                
    return ret