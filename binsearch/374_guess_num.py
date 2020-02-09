# Nathan Zhu Jan 25th, 2020 11:02 pm We had a potluck with Rak and friends tonight at Foundry.
# Leetcode 374 | easy | EZ
# Category: binary search


def guess(num):
    return num == 4 # replace 4 with target.

def guessNumber(n):
    """
    :type n: int
    :rtype: int
    """
    l, r = 1, n
    while l <= r:
        mid = (r - l) // 2 + l
        result = guess(mid)
        
        if result == 0: return mid
        elif result == -1: r = mid - 1
        else: l = mid + 1
            
    return -1