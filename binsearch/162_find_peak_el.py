# Nathan Zhu Jan 27th, 2020 10:18 pm, 376 lecture
# Leetcode 162 | medium | not too bad
# Category: binary search
# 

def findPeakElement(self, arr):
    """
    :type nums: List[int]
    :rtype: int
    """
    N = len(arr)
    left, right = 0, N - 1
    
    def get_val(i):
        if i >= N or i < 0: return float("-inf")
        return arr[i]
        
    while left < right:
        mid = (right - left) // 2 + left
        
        if get_val(mid - 1) < arr[mid] and get_val(mid + 1) < arr[mid]: return mid
        elif arr[mid] < get_val(mid + 1):
            left = mid + 1
        else: right = mid - 1
    return left