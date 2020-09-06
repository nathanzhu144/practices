# /* Nathan Zhu Friday July 24rd, 2020 6:43 am Stockton, CA.  Rak joined leetcode group yesterday.  Also, watching kissing booth 2 apparently.
# *  Leetcode 1310 | medium | easy
# *  Category: presum array
# */


def xorQueries(self, arr, queries):
    """
    :type arr: List[int]
    :type queries: List[List[int]]
    :rtype: List[int]
    """
    N = len(arr)
    presum = arr[:]
    for i in range(1, N): presum[i] ^= presum[i - 1]
        
    ret = []
    for start, end in queries:  # end inclusive
        if start == 0: ret.append(presum[end])
        else: ret.append(presum[start - 1] ^ presum[end])
            
    return ret
        