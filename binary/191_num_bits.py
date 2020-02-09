# Nathan Zhu  Jan 31st, 2020 Duder early morning
# Leetcode 191 | easy | easy
# Category: bits

def hammingWeight(n):
    """
    :type n: int
    :rtype: int
    """
    ret = 0
    while n:
        ret += n & 1
        n >>= 1
    return ret