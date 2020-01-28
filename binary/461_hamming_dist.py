# Nathan Zhu January 26th, 2019 9:30 pm Foundry Lofts
# Leetcode 461 | easy | easy
# Category: bits
#
# We want to find the bitwise hamming distance between two numbers.

def hammingDistance(self, x, y):
    """
    :type x: int
    :type y: int
    :rtype: int
    """
    ret = 0
    xory = x ^ y
    while xory > 0:
        ret += xory & 1
        xory >>= 1
    return ret