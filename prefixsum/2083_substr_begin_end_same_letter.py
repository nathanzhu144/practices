# Nathan Zhu, 12/8/2021, 7:58 pm, Stockton CA
# Leetcode 2083 | medium | EZ
# Category: prefix sum
# Runtime: O(N)
import collections
def numberOfSubstrings(self, s):
    """
    :type s: str
    :rtype: int
    """
    table = collections.defaultdict(lambda: 1)
    ret = 0
    
    for i, ch in enumerate(s):
        ret += table[ch]
        table[ch] += 1
        
    return ret