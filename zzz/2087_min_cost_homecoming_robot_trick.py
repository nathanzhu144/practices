# Nathan Zhu 12/10/2021, 1:31 pm, Stockton, CA
# Leetcode 2087 | medium | opt soln relies on an observation I did not make immediately
#
# Any shortest taxi-cab distance goes through same rows and same cols
# and thus has the same cost.  
def minCost(self, startPos, homePos, rowCosts, colCosts):
    """
    :type startPos: List[int]
    :type homePos: List[int]
    :type rowCosts: List[int]
    :type colCosts: List[int]
    :rtype: int
    """
    r, c = startPos
    er, ec = homePos
    dr, dc = 1 if er > r else -1, 1 if ec > c else -1
    ret = 0
    
    while r != er:
        r += dr
        ret += rowCosts[r]
    
    while c != ec:
        c += dc
        ret += colCosts[c]
        
    return ret