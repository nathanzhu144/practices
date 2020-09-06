# Nathan Zhu Thursday, May 28th, 2020, Stockton CA
# Leetcode 205 | easy | easy
# Category: fizzbuzz


def isIsomorphic(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    table, N = dict(), len(s)
    if len(s) != len(t): return False
    seen = set()
    
    for i in range(N):
        if s[i] not in table:
            if t[i] in seen: return False       # Two chars map to the same char
            seen.add(t[i])
            table[s[i]] = t[i]
        if t[i] != table[s[i]]: return False    # Same char cannot map to two diff chars
            
    return True
            