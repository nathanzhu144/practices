#Write a function to take a positive integer, and return the largest power of two less than or equal to this integer. For example, given the input 5, your function should return 4.

def nearest_power_of_two(n):
    left, right, ret = 0, n, -1

    while left <= right:
        mid = (right - left) // 2 + left
        # see if there's a larger power.
        if 2 ** mid <= n:
            left = mid + 1
            ret = mid
        else:
            right = mid - 1
            
    return 2 ** ret
