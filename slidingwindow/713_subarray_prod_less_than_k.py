# Nathan Zhu in 2nd floor duderstadt overlooking southern road
# Leetcode 713 | medium | not too bad, typical sliding window.
# Category: Sliding window.

def numSubarrayProductLessThanK(arr, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """    
    if not arr: return 0

    currprod = 1
    left, right, ret = 0, 0, 0

    while right < len(arr):
        currprod *= arr[right]

        # We NEED all 3 conditions
        # left has to stay in bounds (right isn't always in bounds)
        while left < len(arr) and left <= right and currprod >= k:
            currprod /= arr[left]
            left += 1
        ret += right - left + 1

        right += 1

    return ret