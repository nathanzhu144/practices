# Nathan Zhu January 29th, 2020 Aboutta go to Coco, Thursday evening at Courtyards
# Leetcode 1074 | hard | hard if not done before
# Category: Presum
# I like this question.  This is similar to largest submatrix sum less than k

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
    for sc in range(C):
        row = [0 for r in range(R)]
        for ec in range(sc, C):
            for r in range(R): row[r] += matrix[r][ec]
            
            table = collections.defaultdict(int)
            table[0] = 1
            presum = 0
            for num in row:
                presum += num
                if presum - target in table: ret += table[presum - target]
                table[presum] += 1
                
    return ret