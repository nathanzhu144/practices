# Nathan Zhu Jan 15th, 2019
# Leetcode 1049 | medium | effing hard dude
# Category: DP 

# This question took me like 5-6 hours to actually understand.
# Long story short you first have to convince yourself that
# this problem breaks down into finding the minimum difiference between
# two subsets, "the easiest hard problem"
# This is doable with pseudopolynomial time with DP

def lastStoneWeightII(self, arr):
    """
    :type stones: List[int]
    :rtype: int
    """
    #       [2, 7, 9, 4, 4]
    # n = 0, 1, 2, 3, 4, 5
    # n represents position we can choose up to
    n, tot = len(arr), sum(arr)
    table = [[0 for c in range(tot + 1)] for r in range(n + 1)]
    
    # with a n of 0, we can only make a sum of 0
    for c in range(1, tot + 1): table[0][c] = 0
    
    # with a sum of 0, we can only make that with any n 
    # by not choosing any of the elements.
    for r in range(n + 1): table[r][0] = 1
    
    for r in range(1, n + 1):
        for c in range(1, tot + 1):
            # If rth element is excluded
            table[r][c] = table[r - 1][c]
            # If rth element is included
            if c >= arr[r - 1]: 
                table[r][c] |= table[r - 1][c - arr[r - 1]]
    
    ret = tot // 2
    while ret >= 0:
        if table[n][ret] == 1: return tot - ret * 2
        ret -= 1
    return tot