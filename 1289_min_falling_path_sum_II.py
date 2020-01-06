# Nathan Zhu, December 26th, 2019, 9:18 pm, 
# Leetcode 1289 | hard | yeah hard
# Category: DP
# Same as paint fence II
# 
# 
import heapq

# Intuition:
# In a row of numbers, an optimal path will use one of the two smallest numbers in that row.
# This is because we can only ban one of the columns, so even if we ban the column with smallest,
# we will definitely use second smallest number.
#
# The in-efficient DP soln does a DP based off of the idea of, "given that we have banned column i,
# what's the best soln from this index"
# 

# Bad part, writes on arr array. 
# efficient soln
def minFallingPathSum(arr):
    """
    :type arr: List[List[int]]
    :rtype: int
    """
    for row in range(1, len(arr)):
        two_smallest = heapq.nsmallest(2, arr[row - 1])
        
        for col in range(len(arr)):
            if arr[row - 1][col] == two_smallest[0]:
                arr[row][col] += two_smallest[1]
            else:
                arr[row][col] += two_smallest[0]
    
    return min(arr[-1])

# recursive DP soln (this times out)
# during an interview, I think this is good enough
def minFallingPathSum_recursive_DP(arr):
    table = dict()
    if not arr: return 0
    
    def helper(arr, ridx, banned_col):
        if ridx >= len(arr): return 0
        
        key = (ridx, banned_col)
        if key in table: return table[key]
        
        ret = float('inf')
        two_smallest = heapq.nsmallest(2, arr[ridx])
        
        # We only recurse on the two smallest costs in the row.
        for col in range(len(arr[ridx])):
            if col != banned_col and arr[ridx][col] in two_smallest:
                ret = min(arr[ridx][col] + helper(arr, ridx + 1, col), ret)
                
        table[key] = ret
        return ret
    
    return helper(arr, 0, None)