# Nathan Zhu Jan 27th, 2019 In 376 lecture, he's talking about Floyd Warshall
# Leetcode 459 | easy | not so easy
# Runtime: O(N)
# Category: Misc tricks
# 
def repeatedSubstringPattern(s):
    """
    :type s: str
    :rtype: bool
    """
    # AA  AA
    # A'AA A'
    
    # AB 
    # A'B B A'
    
    return s in (s * 2)[1:-1]
    # Does in use rabin karp or kmp?