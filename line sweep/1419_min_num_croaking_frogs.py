# Nathan Zhu April 19th, 2020. Stockton, CA Weekly contest 185, position 225 / 9206, a bit above top 2.5%.  First contest to get all 4 qs, also no WAs.
# Leetcode 1419 | medium | kinda hard, but not too bad, a harder medium
# Category: Interval line sweep is most similar tbh.
#           can think of this as a complicated meeting rooms question,
# Tbh the code is kinda messy in this one, I should revisit this; wrote this in a contest
# 

import collections
def minNumberOfFrogs(arr):
    """
    :type croakOfFrogs: str
    :rtype: int
    """
    table = dict()
    table['r'] = 'c'
    table['o'] = 'r'
    table['a'] = 'o'
    table['k'] = 'a'
    c = collections.Counter()
    
    ret = 0
    curr = 0
    num_c, num_k = 0, 0
    for ch in arr:
        if ch == 'c':
            curr += 1
            num_c += 1
            ret = max(ret, curr)
        if ch == 'k':
            num_k += 1
            curr -= 1
        if ch != 'c': 
            if ch not in table: return -1
            c[table[ch]] -= 1    # subtract 1 from prev char
        if ch != 'k': c[ch] += 1           # add 1 to curr char
        if ch in table and c[table[ch]] < 0: return -1
    
    if num_c != num_k: return -1
    for ch in "croa":
        if c[ch] != 0: return -1
    return ret