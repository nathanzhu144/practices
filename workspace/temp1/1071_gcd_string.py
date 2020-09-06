# Nathan Zhu, Stockton, CA. June 14th, 2020.  6:28 pm.
# Leetcode 1071 | easy | medium
# Category: Math

def gcdOfStrings(str1, str2):
    """
    :type str1: str
    :type str2: str
    :rtype: str
    """
    def gcd(a, b):
        if a == 0: return b
        if b == 0: return a
        return gcd(b, a % b)
    
    # does the helper ever make more than 1 recursive call?
    def helper(s1, s2):
        print(s1, s2)
        if s1 + s2 != s2 + s1: return ""
        elif s1 == s2: return s1
        else:
            n = gcd (len(s1), len(s2))
            return helper(s1[:n], s2[:n])
        
    return helper(str1, str2)