# Nathan Zhu March 30th, 2020.  4:37 am.  Last Monday living in Foundry Lofts in my life I think.  WE are heading home next sunday
# Leetcode 28 | easy | HARD
# Category: KMP / Rabin-karp 

def repeatedSubstringPattern(s):
    """
    :type s: str
    :rtype: bool
    """
    return s in (s * 2)[1:-1]