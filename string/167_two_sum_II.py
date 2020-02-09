
# Nathan Zhu 11:42 pm, December 31st, 2019 Won like 5 stuffed animals today at Santa Cruz boardwalk, good day.  New years and leetcode. 
# Leetcode 167 | easy | EZ
# Category: Sliding window
# Idea here is to do two-sum in O(1) space O(N) time unlike hash table approach.

def twoSum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    N = len(numbers)
    left, right = 0, N - 1
    
    while left < right:
        if numbers[left] + numbers[right] == target: 
            ret = [left + 1, right + 1]
            left += 1
            right -=1
            return ret
        elif numbers[left] + numbers[right] < target: left += 1
        else: right -= 1
            
    return []