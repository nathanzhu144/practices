# Nathan Zhu April 9th, 2020 12:22 am Stockton, CA, COVID-19
# Leetcode 266 | easy | easy
# Category: misc-tricks

import collections


def canPermutePalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    c = collections.Counter(s)
    
    num_odd = 0
    for key, val in c.items():
        if val & 1: num_odd += 1
        if num_odd > 1: return False
    return True