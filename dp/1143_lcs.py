# Nathan Zhu January 31st, 2019 9:30 pm, at bdubs talking about Hershal's relationship problems with Peifu, Nafeez, and I.
# Leetcode 1143 | medium | easy
# Category: DP
# LCS my old friend.

def longestCommonSubsequence(text1, text2):
    """
    :type text1: str
    :type text2: str
    :rtype: int
    """
    table = dict()
    def helper(s1, s2, i1, i2):
        if len(s1) == i1 or len(s2) == i2: return 0
        key = (i1, i2)
        if key in table: return table[key]
        if s1[i1] == s2[i2]: table[key] = 1 + helper(s1, s2, i1 + 1, i2 + 1)
        else: table[key] = max(helper(s1, s2, i1 + 1, i2), helper(s1, s2, i1, i2 + 1))
        return table[key]
    
    return helper(text1, text2, 0, 0)
        