# Nathan Zhu April 4th, 2020. Foundry Lofts, Final Week, COVID-19
# Leetcode 1400 | medium | medium
# Category: misc tricks
# 
# 

import collections

def canConstruct(self, s, k):
    """
    :type s: str
    :type k: int
    :rtype: bool
    """
    c = collections.Counter(s)
    
    odds = 0
    for ch, count in c.items():
        if count % 2 == 1:
            odds += 1
    
    return odds <= k and k <= len(s)