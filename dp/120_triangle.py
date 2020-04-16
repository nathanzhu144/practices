# Nathan Zhu April 11th, 2020 11:03 am, Stockton, CA, COVID-19
# Leetcode 120 | medium | medium
# Category: DP

def minimumTotal(triangle):
    """
    :type triangle: List[List[int]]
    :rtype: int
    """
    def helper(r, c):
        key = (r, c)
        if r < 0 or c < 0 or c >= len(triangle[r]): return float('inf')
        if r == 0 and c == 0: return triangle[0][0]
        if key in table: return table[key]
        ret = min(helper(r - 1, c - 1), helper(r - 1, c)) + triangle[r][c]
        table[key] = ret
        return ret
        
    table = dict()
    ret = float('inf')
    for c in range(len(triangle[-1])):
        ret = min(ret, helper(len(triangle) - 1, c))
        
    return ret