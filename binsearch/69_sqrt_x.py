# Nathan Zhu 11:44 pm, June 27th, 2019, Amex Building, 36th Floor, focus room
# Leetcode 69 | easy | binary search problems aren't easy
#
# The intuition here is we want to use binary search to find the floored square root of a number.
# so sqrt(8) = 2, sqrt(4) = 2, sqrt(9) = 3
#
# If you think about it, this is a disguised upper bound problem.  
# We are trying to find the biggest int "j", 1 <= j <= such that j <= j / mid
#

def binary_sqrt(x):
    # stops a division by 0, if x is 0
    if x == 0: return 0

    l, r = 1, x
    ans = -1
    # I'm pretty sure we need the <=.  Suppose we do binary_sqrt(1).
    # l == r, until we go into else statement.  
    while l <= r:
        mid = (r - l) // 2 + l
        # if mid > x / mid, sqrt definitely cannot be that value
        if mid > x / mid:
            r = mid - 1
        # we are trying to find the biggest number s.t. mid <= x / mid, so we save the ans
        # and try to search 1 greater
        else:
            ans = mid
            l = mid + 1

    return ans


if __name__ == "__main__":
    print(binary_sqrt(9))
    print(binary_sqrt(8))
    print(binary_sqrt(5))
    print(binary_sqrt(4))