# Nathan Zhu Aug 27th 2019 2:14 am at Stockton Cali
# Leetcode 278 | easy | EZ
# Category: binary search
# 
# Done in real-time in a "google phone interview", time limit 1hr 30 for 2 questions
# Rating was 7.69/10, beating 92% of all users.
# 
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

# This is a standard binary search.

def firstBadVersion(n):
    """
    :type n: int
    :rtype: int
    """
    left, right = 0, n
    ret = -1
    while left <= right:
        mid = (left + right) // 2
        if isBadVersion(mid): 
            ret = mid
            right = mid - 1
        else:
            left = mid + 1
            
    return ret278