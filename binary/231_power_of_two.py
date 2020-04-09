# // Nathan Zhu March 19th, 2020 10:19 pm Foundry Lofts, it is spring break
# // Leetcode 231 | easy | easy
# // Category: binary

def isPowerOfTwo(n):
    """
    :type n: int
    :rtype: bool
    """
    return n != 0 and n & n - 1 == 0