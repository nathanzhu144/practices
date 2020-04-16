# Nathan Zhu Sunday Feb 16th, 2020 11:37 pm, Foundry Lofts Day after birthday.  Did 376 practice exams today.
# Leetcode 242 | easy | EZ
# Category: Fizzbuzz

import collections
def isAnagram(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    return collections.Counter(s) == collections.Counter(t)