# Nathan Zhu Friday December 26th, 2019 9:36 pm
# Leetcode 931 | medium | sure medium
# Category: DP 
# https://leetcode.com/problems/minimum-falling-path-sum/discuss/186689/Java-DP-solution-with-graph-illustrated-explanations
#
# The optimal way involves modifying the input graph (see above)
#
# However, I end up constraining the search space to row * col, where col
# represents assumes that we have a falling path through this column

def minFallingPathSum(A):
    """
    :type A: List[List[int]]
    :rtype: int
    """
    
    table = dict()
    def helper(A, row, col):
        if row == -1: return 0
        key = (row, col)
        if key in table: return table[key]
        
        ret = float('inf')
        # from this col, we can move left, up, right
        for dcol in [-1, 0, 1]:
            newcol = dcol + col
            if 0 <= newcol < len(A):
                ret = min(ret, A[row][col] + helper(A, row - 1, newcol))
        table[key] = ret
        return ret
    
    min_sum = float('inf')
    for i in range(len(A)):
        min_sum = min(helper(A, len(A) - 1, i), min_sum)
        
    return min_sum
        
        
                
                