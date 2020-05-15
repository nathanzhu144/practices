# Nathan Zhu May 4th, 2020.  Damn I still remember doing this question at Renying's place at willow tree a year and a half ago
#                            Just finished 376 final, did above aveage.
# Leetcode 11 | medium | medium
# Category: sliding window


def maxArea(arr):
    """
    :type height: List[int]
    :rtype: int
    """
    N = len(arr)
    left, right = 0, N - 1
    ret = 0
    
    while left <= right:
        ret = max(ret, (right - left) * min(arr[left], arr[right]))
        if arr[left] > arr[right]:
            right -= 1
        else:
            left += 1
            
    return ret