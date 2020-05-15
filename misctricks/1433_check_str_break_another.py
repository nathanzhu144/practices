# Nathan Zhu April 2nd, 2020 Biweekly contest
# Leetcode 1433 | medium | description kinda confusing, not bad tho
# Category: misc tricks

import string
import collections

def checkIfCanBreak(self, s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: bool
    """
    def helper(s1, s2):
        c1, c2 = collections.Counter(s1), collections.Counter(s2)
        num1, num2 = 0, 0

        for ch in string.ascii_lowercase[::-1]:
            num1 += c1[ch]
            num2 += c2[ch]
            if num1 > num2: return False
        return True
    return helper(s1, s2) or helper(s2, s1)