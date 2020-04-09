# Nathan Zhu April 9th, 2020.  12:22 am, Stockton, CA, COVID-19
# Leetcode 594 | easy | easy
# Category: Misc tricks


import collections
def findLHS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # 1 3 2 2 5 2 3 7
    
    counts = collections.Counter()
    c = collections.defaultdict(set)
    for i, num in enumerate(nums):
        c[num].add(num)
        counts[num] += 1
        c[num - 1].add(num)
        counts[num - 1] += 1
        
    ret = 0
    for key, val in c.items():
        if key in val and key + 1 in val:
            ret = max(counts[key], ret)
    return ret