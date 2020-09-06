# Nathan Zhu Thursday July 30th, 2020 7:03 am, Stockton CA.  Final presentation prep at Salesforce.  Went running in morning today.
# Leetcode 1262 | medium | kinda chllenging
# Category: 1D DP
# Runtime: O(3 * N) 
# 

import collections

#         Ex. [3,6,5,1,8]

    
#         [3, -inf, -inf]   3
#         [9, -inf, -inf]   6
#         [9, -i, 14]       9
#         [15, 10, 14]      1
#         [18, 22, 23]      8
#
#         [largest mod 0, largest mod 1, largest mod 2] up to this point.
def maxSumDivThree(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    table = [0, float('-inf'), float('-inf')]
    N = len(nums)
    
    for i, num in enumerate(nums):
        ntable = table[:]
        for i in range(3):
            ntable[(i + num) % 3] = max(ntable[(i + num) % 3], table[i] + num)
        table = ntable
        
    return table[0]
if __name__ == "__main__":
    print(maxSumDivThree([3,6,5,1,8]))
