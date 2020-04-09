# Nathan Zhu April 9th, 2020, Stockton, CA, 7:18 am
# Leetcode 1296 | medium | medium
# Category: Greedy

import collections

def isPossibleDivide(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    c = collections.Counter(nums)
    
    for num in c:
        start = num
        while c[start - 1]: start -= 1
            
        while start <= num:
            times = c[start]
            
            if times > 0:
                for victim in range(start, start + k):
                    if c[victim] < times: return False
                    c[victim] -= times
            start += 1
    return True