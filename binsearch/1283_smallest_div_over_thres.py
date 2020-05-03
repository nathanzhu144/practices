# Nathan Zhu April 23rd, 2020 COVID-19 stockton CA, 376 exam in a week
# Leetcode 1283 | medium | not bad
# Category: binary search

def smallestDivisor(arr, threshold):
    """
    :type nums: List[int]
    :type threshold: int
    :rtype: int
    """
    def currval(arr, div):
        return sum([(num + div - 1) // div for num in arr])
    
    left, right = 1, max(arr)
    ret = -1
    while left <= right:
        mid = (right - left) // 2 + left
        curr = currval(arr, mid)
        if curr <= threshold: 
            ret = mid
            right = mid - 1
        else: left = mid + 1
            
    return ret