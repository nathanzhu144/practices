# Nathan Zhu 11:09 pm December 27th, 2019 Just got back from Napa Valley, hot air ballooning and napa valley today
# Leetcode 1064 | easy | EZ
# Category: binary search

# Given an array A of distinct integers sorted in ascending order, return the smallest
#  index i that satisfies A[i] == i.  Return -1 if no such i exists.

 
def fixedPoint(A):
    """
    :type A: List[int]
    :rtype: int
    """
    ret = -1
    left, right = 0, len(A) - 1
    while left <= right:
        mid = (right - left) // 2 + left
        if A[mid] == mid:
            ret = mid
            right = mid - 1
        elif A[mid] < mid:
            left = mid + 1
        elif A[mid] > mid:
            right = mid - 1
            
    # In the case of an array like [-5, -2, -1] ret will be -1 at end
    # In the case of an array like [5, 6, 7], ret will be -1 at end
    # In the case an array like [-3, -2, 1, 7] ret will be inside bounds of array, but will not be at an index where arr[i] == i
    # therefore, we check both conditions
    if ret == -1 or A[ret] != ret: return -1
    else: return ret