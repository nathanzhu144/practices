# Nathan Zhu May 1st, 2020. Finished 376 final 3 days ago, watched code-8 with hershal and crew today
# Leetcode 311 | medium | medium/hard
# Category: Misc tricks
#
# I literally had to learn a whole new way of matrix multiplication to do this damn question, it is beautiful.
# See the explanation sheet for details
# 

import collections
def multiply(A, B):
    """
    :type A: List[List[int]]
    :type B: List[List[int]]
    :rtype: List[List[int]]
    """
    if not A or not B: return []  # empty matrices cannot be mult
    ra, ca, rb, cb = len(A), len(A[0]), len(B), len(B[0])
    if ca != rb: raise(Exception('Not right dimensions'))
    
    table_a, table_b = collections.defaultdict(dict), collections.defaultdict(dict)
    ret = [[0 for c in range(cb)] for r in range(ra)]

    for r in range(ra):
        for c in range(ca):
            if not A[r][c]: continue
            table_a[r][c] = A[r][c]
            
    for r in range(rb):
        for c in range(cb):
            if not B[r][c]: continue
            table_b[r][c] = B[r][c]
            
    for i, table in table_a.items():
        for k, val1 in table.items():
            if k not in table_b: continue
            for j, val2 in table_b[k].items():
                ret[i][j] += val1 * val2
                
    return ret