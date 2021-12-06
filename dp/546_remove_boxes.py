# Nathan Zhu, 12/6/2021, 1:02 pm, Stockton, Ben Holt Starbucks, deciding between SF and BBG among others.  
# Leetcode 546 | hard | very challenging
# Category: DP
# Runtime: N^4, for each of the N^3 solns, we have to loop O(N) to compute the result
# Space: N^3  

#  Intuition
# Breaking up a consecutive sequence of numbers never works optimally
# because when (A + B) ^ 2 > A ^ 2 and B ^ 2 when A, B > 0
# l = left idx inclusive
# r = right idx inclusive
# k = number of numbers same as left
# Ex. 
#     [2, 2, 2, 2, 3, 4, 2, 2, 5, 5, 2]   arr
#      0  1  2  3  4  5  6  7  8  9  10   idx
#      -  -  -  -
#      1  2  3  4  (k = 4)
# Intuitively, we always have a sequence of same numbers at the beginning of length k
# k = 4 here because we have 4 different 2s starting the array
# 
# Choice 1:
# In this case, we have 3 choices with all of the 2s in the beginning.
# Ex. [2, 2, 2, 2, 3, 4, 2, 2, 5, 5, 2]   arr
#      -  -  -  -  4  5  6  7  8  9 10    idx
#        4 * 4    + dp(l = 4, r = 10, k = 0)
# 
# Choice 2:
# Ex. [2, 2, 2, 2, 3, 4, 2, 2, 5, 5, 2]   arr
#      -  -  -  -  4  5  -  -  8  9 10    idx
#             \          /
#               combine these 2s
#           dp(l = 4, r = 5, k = 0) + dp(l = 6, r = 10, k = 4)
# 
# Choice 3:
# Ex. [2, 2, 2, 2, 3, 4, 2, 2, 5, 5, 2]   arr
#      -  -  -  -  4  5  6  7  8  9  -    idx
#             \                     /
#                 combine these 2s
#           dp(l = 4, r = 9, k = 0) + dp(l = 10, r = 10, k = 4)
#

def removeBoxes(boxes):
    """
    :type boxes: List[int]
    :rtype: int
    """
    table = dict()
    def helper(l, r, k):
        if l > r: return 0
        
        key = (l, r, k)
        if key in table: return table[key]
        
        num_left = k
        while l < r and boxes[l] == boxes[l + 1]:
            num_left += 1
            l += 1
        
        ret = (num_left + 1) * (num_left + 1) + helper(l + 1, r, 0)
        for div in range(l + 1, r + 1):
            if boxes[div] == boxes[l]:
                ret = max(ret, helper(l + 1, div - 1, 0) + helper(div, r, num_left + 1))
        
        table[key] = ret
        return ret
    return helper(0, len(boxes) - 1, 0)