# Nathan Zhu April 9th, 2020 7:24 am
# Leetcode 416 | medium | medium
# Category: DP
# There's a backtracking soln, and there's a DP soln, this is the DP soln.

def canPartition(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    # [1, 3]
    # 
    #     0  1  2 
    #  0  T  T  T
    #  1
    #  2  
    #  3
    #  4
    # sums 
    
    tot = sum(nums)
    if tot & 1: return False   # If num is odd, cannot be partitioned
    
    N = len(nums) + 1
    sums = tot // 2 + 1
    table = [[False for c in range(N)] for r in range(sums)]
    
    # We can trivially make a sum of 0 with nothing.
    for c in range(N):
        table[0][c] = True
        
    for r in range(1, sums):
        for c in range(1, N):
            table[r][c] = table[r][c - 1] if c != 0 else False
            if r - nums[c - 1] >= 0 and c > 0:
                table[r][c] |= table[r - nums[c - 1]][c - 1]
                
    return table[tot // 2][-1] 