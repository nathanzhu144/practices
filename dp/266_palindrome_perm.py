# Nathan Zhu January 2nd, 2019 11:27 pm Got back from Monterey yesterday, point lobos.  Had to park on side of freeway.
# Leetcode 266 | easy | literally coded in 45 seconds, and passed on first try.
#
# A string can be a palindrome iff at most one the counts of its characters are odd.

import collections
def canPermutePalindrome(self, s):
    """
    :type s: str
    :rtype: bool
    """
    c = collections.Counter(s)
    odd_left = 1
    for key in c: 
        if c[key] % 2 == 1: odd_left -= 1
        if odd_left < 0: return False
    return True