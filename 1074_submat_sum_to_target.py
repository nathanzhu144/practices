# Nathan Zhu 9:!4 am January 17th, 2019 Duderstadt library 2nd floor, next to the flags, overlookin the pottery building
# Leetcode 1074 | hard | yeah pretty hard 
#
# Insights.  
# Brute force is N^4 with a pre-sum table for all the elements and would be N^6 if we do not use a presum
# where N^2 comes from summing the elements.
#
# We can reduce to N^3 by using the same idea as subarray sum equals k.  Assuming we fix a start col, end col,
# we can keep a hash table of all of the sums we have seen so far of that slice, and if we see an old prefix  sum
# in the table, we can add as necessary.

import collections

def numSubmatrixSumTarget(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: int
    """
    if not matrix or not matrix[0]: return 0
    
    R, C = len(matrix), len(matrix[0])
    ret = 0
    
    for r in range(R):
        for c in range(1, C):
            matrix[r][c] += matrix[r][c - 1]
    
    # sc, ec stands for "start col", "start col"
    # for matrices we are looking at
    # ec is inclusive, sc is inclusive.
    
    #  [0, 0, 0, 0]
    #  [0, 1, 1, 0]
    #  [0, 1, 1, 0]
    #  [0, 0, 0, 0]
    #     sc ec
    #  sc = 1, ec = 2
    for sc in range(C):
        for ec in range(sc, C):]
            # Key to map is a prefix sum
            # value to map is count (num of appearances) of each prefix sum we have seen so far
            # an empty submatrix trivially has a sum of 0
            table = collections.defaultdict(int)
            table[0] = 1
            
            curr = 0
            for r in range(R):
                curr += matrix[r][ec]
                if sc - 1 >= 0:
                    curr -= matrix[r][sc - 1]

                ret += table[curr - target]
                table[curr] += 1
            
    return ret

if __name__ == "__main__":
    print(numSubmatrixSumTarget([[1,-1],[-1,1]], 0))