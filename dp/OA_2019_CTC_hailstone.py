# Nathan Zhu August 5th, 2019 3:00 pm
# Category: DP
#
# This was in the OA for Chicago trading.  3 hour time limit.
#
# We want to find the longest hailstone sequence from [1 ... N], where N is inclusive
# and 1 <= N <= 1000000

def hailstone(X):
    # Table for memoizing earlier CTC sequences
    table = dict()
    
    # Recursive function for calculating length of CTC sequence
    def helper(num):
        if num in table: return table[num]
        if num == 1: return 1
        
        # If this is even
        if num % 2 == 0: table[num] = 1 + helper(num // 2)
        # If this is odd
        else: table[num] = 1 + helper(3 * num + 1)
        return table[num]
    
    # We attempt to do CTC sequences from 1 -> X (inc)
    count = 0
    ret = -1
    for i in range(1, X + 1):
        newcount = helper(i)
        if newcount > count:
            count = newcount
            ret = i
    
    return ret