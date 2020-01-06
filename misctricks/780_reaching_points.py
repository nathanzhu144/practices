# Nathan Zhu Monday 8:06 am
# Leetcode 780 | hard | yeah hard
# Category: Misc tricks
# The insight to solve this efficiently in LogN time are fascinating to say the least.
#
# A Naive solution is to attempt a BFS, but that has 2^N efficiency worst case.  
# However, keeping a visited set of nodes probably can bound it to N^2 space and time where
# N is the bigger of sx, and sy. 
#
# A better solution is to realize that from sx, sy there are 2 possible paths at each sx, sy,
# but from tx, ty you can only move backwards one way.  This results in an O(N) solution.
#
# However, this can be reduced to LogN with some modulo madness.  The idea is that instead of subtracting,
# we use mod.
#  
# 


# O(N) efficiency
def reachingPoints(sx, sy, tx, ty):
    """
    :type sx: int
    :type sy: int
    :type tx: int
    :type ty: int
    :rtype: bool
    """
    def helper(sx, sy, tx, ty):
        if sx == tx and sy == ty: return True
        if tx < sx or ty < sy: return False
        if tx == ty: return False                       # this line prevents infinite recursions.
        
        if tx > ty: return helper(sx, sy, tx - ty, ty)
        if ty > tx: return helper(sx, sy, tx, ty - tx)
        
    return helper(sx, sy, tx, ty)

# Log N efficiency
def reachingPointsEff(sx, sy, tx, ty):
    """
    :type sx: int
    :type sy: int
    :type tx: int
    :type ty: int
    :rtype: bool
    """
    # doing it like this results in a bug, infinite loop for cases where tx == ty
    # while tx > sx and ty > sy:
    #     if tx > ty: tx = tx % ty
    #     elif ty > tx: ty = ty % tx
    
    # this fixes it
    while sx < tx and sy < ty:
        tx, ty = tx % ty, ty % tx

    # Note, we have to check if ty >= sy, and tx >= sx
    return sx == tx and (ty - sy) % sx == 0 and ty >= sy or \
            sy == ty and (tx - sx) % sy == 0 and tx >= sx

if __name__ == "__main__":
    print(reachingPointsEff(1, 6, 11, 10))