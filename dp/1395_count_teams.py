# Nathan Zhu May 28th, 2020. 10:00 pm, COVID-19, Foundry, in Leetcode contest
# Leetcode 1395 | medium | not bad
# Category: Backtrackingg / DP
# 

import collections

def numTeams(rating):
    """
    :type rating: List[int]
    :rtype: int
    """
    # 1, 2, 3, 4
    # 
    ret = [0]
    N = len(rating)
    
    def helper(arr, i, currlen, bar, asc):
        if currlen == 3: 
            ret[0] += 1
            return
        if i == N: return
        
        if (asc and arr[i] > bar) or (not asc and arr[i] < bar):
            helper(rating, i + 1, currlen + 1, arr[i], asc)
            helper(rating, i + 1, currlen, bar, asc)
        else:
            helper(rating, i + 1, currlen, bar, asc)
            
    for i, num in enumerate(rating):
        helper(rating, i + 1, 1, rating[i], True)
        helper(rating, i + 1, 1, rating[i], False)
    return ret[0]