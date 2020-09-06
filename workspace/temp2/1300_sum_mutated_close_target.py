# Nathan Zhu Monday July 27th, 2020 9:54 am, Stockton CA.  GOT POSITION #36/14309 for top 0.25% in Weely Contest 199.
#                                                          Last 2 weeks of SF internship.  :O  
# Leetcode 1300 | medium | medium
# Category: Binary search
# Runtime: Nlog(Max(A))
# 

import collections

def findBestValue(arr, target):
    """
    :type arr: List[int]
    :type target: int
    :rtype: int
    """

    def helper(arr, num):
        return sum([n if n <= num else num for n in arr])

    left, right = 0, max(arr)
    ret = [[-1, float('inf')], [-1, float('inf')]]  # ret[0] is one on smaller side, ret[1] is one on bigger side
                                # ret[0][0] is numbe itself, ret[0][1] is delta between num and target
    while left <= right:
        mid = (right - left) // 2 + left
        res = helper(arr, mid)
        if res <= target:
            ret[0][0] = mid
            ret[0][1] = abs(res - target)
            left = mid + 1
        else: right = mid - 1

    left, right = 0, target
    while left <= right:
        mid = (right - left) // 2 + left
        res = helper(arr, mid)
        if res >= target:
            ret[1][0] = mid
            ret[1][1] = abs(res - target)
            right = mid - 1
        else: left = mid + 1

    if ret[0][1] <= ret[1][1]: return ret[0][0]
    else: return ret[1][0]


# [2,3,5]
# 10
# 2 3 5
# 
# 


# 4 9 3
# 3 3 3  = 9
# 4 4 3  = 11
# 

if __name__ == "__main__":
    #print(findBestValue([4,9,3], 10))
    print(findBestValue([2, 3, 5], 11))