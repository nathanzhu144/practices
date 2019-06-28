#  Nathan Zhu 12:03 am, June 28th, 2019 Amex Tower, 36th floor in a dark focus room
#  Leetcode 367 | easy | I think easy
#  So, you can find whether a square is a perfect square in logn time.
#  It is actually really easy... I finished it in ~2 min.
# 


def is_perfect_sq(num):
    """
    :type num: int
    :rtype: bool
    """
    low, high = 0, num
    
    while low <= high:
        mid = (high - low) / 2 + low
        
        # if mid squared is num, we know it is a perfect square
        if mid ** 2 == num: return True
        # if mid squared is greater htan num, we need to look at things smaller than mid
        if mid ** 2 > num: high = mid - 1
        # if mid square is less than num, we need to look at things greater than mid
        if mid ** 2 < num: low = mid + 1
    
    # if we exit, we know low = high - 1, and that when
    # low == high == mid, it is not true that mid ** 2 == num, cannot
    # be a perfect square
    return False