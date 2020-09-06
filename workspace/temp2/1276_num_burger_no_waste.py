
# Nathan Zhu Tuesday July 28th, 2020 8:00 am, Stockton CA.  GOT POSITION #36/14309 for top 0.25% in Weely Contest 199.
#                                                          Last 2 weeks of SF internship.  :O  Met up with Katie, also Dara/Austin yesterday
#                                                          Kaushal has good hummingbird pics.
# Leetcode 1276 | medium | alright
# Category: binary search, math
# Runtime: O(logn)
# 
# There's an O(1) solution with a system of linear equations.  Just thought of the logn soln
# first.  I thought the logn soln was really smart.

import collections


def numOfBurgers(self, tom, cheese):
    """
    :type tomatoSlices: int
    :type cheeseSlices: int
    :rtype: List[int]
    """
    ret = [[]]
    
    # t - 2 * c > 0: more jumbo burgers
    # t - 2 * c == 0: perfect
    # t - 2 * c < 0: fewer jumbo burgers
    def possible(jumbo, t, c):
        t -= 4 * jumbo
        c -= 1 * jumbo
        
        res = t - 2 * c
        if res == 0: ret[0] = [jumbo, c]
        return res
    
    
    left, right = 0, tom // 4
    while left <= right:
        mid = (right - left) // 2 + left   # mid is num jumbo burgers
        res = possible(mid, tom, cheese)
        if res == 0: return ret[0]
        elif res > 0: left = mid + 1
        else: right = mid - 1
            
    return []