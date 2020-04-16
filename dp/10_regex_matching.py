# Nathan Zhu April 7th, 2020, 12:01 am Foundry Lofts, COVID-19
# Leetcode 10 | hard | hard
# Category: DP
# 
def isMatch(s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    def is_empty(s):
        if len(s) & 1 != 0: return False
        for i in range(len(s)):
            if i & 1 and s[i] != "*": return False
        return True
    
    table = dict()
    def helper(s, p, si, pi):
        if si == -1 or pi == -1:
            return si == -1 and is_empty(p[:pi + 1])
        
        key = (si, pi)
        if key in table: return table[key]
        ret = False
        if p[pi] == "." or s[si] == p[pi]:
            ret = helper(s, p, si - 1, pi - 1)
        elif p[pi] == "*":
            if (p[pi - 1] == "." or s[si] == p[pi - 1]):
                ret = helper(s, p, si - 1, pi) or helper(s, p, si, pi - 2)
            else:
                ret = helper(s, p, si, pi - 2)
        else: 
            ret = False
            
        table[key] = ret
        return ret
    
    return helper(s, p, len(s) - 1, len(p) - 1)