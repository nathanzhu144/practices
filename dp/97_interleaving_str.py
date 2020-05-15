# Nathan Zhu May 7th, 2020. Saw Amber today while walking with Renying, they are abouta have finals.
# Leetcode 97 | hard | easy
# Category: DP
#
# Classic M * N string DP


def isInterleave(s1, s2, s3):
    """
    :type s1: str
    :type s2: str
    :type s3: str
    :rtype: bool
    """
    table = dict()
    def helper(s1, s2, target):
        key = (s1, s2)
        if key in table: return table[key]
        if not s1: return s2 == target
        if not s2: return s1 == target
        
        table[key] = False
        if s1[0] == target[0] or s2[0] == target[0]:
            if s1[0] == target[0]:
                table[key] |= helper(s1[1:], s2, target[1:])
            if s2[0] == target[0]:
                table[key] |= helper(s1, s2[1:], target[1:])
        return table[key]
    
    return helper(s1, s2, s3)