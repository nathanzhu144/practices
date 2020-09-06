# Nathan Zhu, May 30th, 2020, Stockton, CA, during morning lc contest
# Leetcode 1460 | medium | cool
# Category: Misc tricks
# Insight, vertical and horizontal cuts don't influence each other, so optimize separately.
# To get first and last cuts, add 0, and height, weight into the arrays

def maxArea(h, w, hc, vc):
    """
    :type h: int
    :type w: int
    :type horizontalCuts: List[int]
    :type verticalCuts: List[int]
    :rtype: int
    """
    MOD = 10 ** 9 + 7
    h, v = sorted([0] + hc + [h]), sorted([0] + vc + [w])
    maxr, maxc = 0, 0
    for i in range(len(h) - 1):
        maxr = max(maxr, h[i + 1] - h[i])
    for i in range(len(v) - 1):
        maxc = max(maxc, v[i + 1] - v[i])
        
    return (maxr * maxc) % MOD
    