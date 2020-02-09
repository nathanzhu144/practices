# Nathan Zhu Feb 1st, 2020. 9:45 pm. Foundry Lofts.
# Leetcode 44 | hard | hard?
# Category: DP
# Runtime N^2

def isMatch(s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    
    def empty(s):
        for ch in s:
            if ch != "*": return False
        return True

    table = dict()
    
    def helper(s, p, si, pi):
        if len(p) == pi: return len(s) == si
        if len(s) == si: return empty(p[pi:])
        
        key = (si, pi)
        if key in table: return table[key]
        
        if p[pi] == "?" or s[si] == p[pi]:
            table[key] = helper(s, p, si + 1, pi + 1)
        elif p[pi] == "*":
            table[key] = helper(s, p, si + 1, pi) or helper(s, p, si, pi + 1)  
        else: table[key] = False
            
        return table[key]
    
    return helper(s, p, 0, 0)
        