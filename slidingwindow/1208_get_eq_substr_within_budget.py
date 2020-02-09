# Nathan Zhu Jan 26th, 2019 8:52 pm
# Leetcode 1208 | medium | not bad
# Category: Sliding window.

def equalSubstring(self, s, t, maxCost):
    """
    :type s: str
    :type t: str
    :type maxCost: int
    :rtype: int
    """
    N = len(s)
    ret = 0
    l, r = 0, 0
    budget = maxCost
    while r < N:
        budget -= abs(ord(s[r]) - ord(t[r]))
        r += 1
        
        while budget < 0:
            budget += abs(ord(s[l]) - ord(t[l]))
            l += 1
        
        ret = max(ret, r - l)
        
    return ret