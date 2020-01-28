# Nathan Zhu January 27th, 2020 11:21 am SI 106 class
# Leetcode 562 | medium | med
# Category: Misc tricks
#

import collections
import itertools
def longestLine(M):
    if not M or not M[0]: return 0
    
    def helper(arr):
        ret, cnt = 0, 0
        for n in arr:
            if n == 0: cnt = 0
            if n == 1:
                cnt += 1
                ret = max(cnt, ret)
                
        return ret
    
    table = collections.defaultdict(list)
    for r, row in enumerate(M):
        for c, val in enumerate(row):
            table[(1, r - c)].append(val)  # diagonal
            table[(2, r + c)].append(val)  # anti-diag
            table[(3, r)].append(val)
            table[(4, c)].append(val)
            
    return max(map(helper, table.values()))

if __name__ == "__main__":
    print(longestLine([[0,1,1,0],
                       [0,1,1,0],
                       [0,0,0,1]]))