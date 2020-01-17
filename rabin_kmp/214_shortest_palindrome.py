# Nathan Zhu January 15th, 2020 5:30 pm Wes Weimer is rating about some weird ass coding metrics, nearly got hit by candy earlier when I vowed to stop drinking coffee (for cancer)
# Leetcode 214 | hard | hard
# This problem basically is a KMP problem, but I don't know KMP, but
# one soln with the same runtime is actually Rabin-Karp rolling hash.  I know how to do that!
#
# 
def shortestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    if not s: return s
    
    PRIME, power = 10 ** 9 + 7, 1
    hash1, hash2 = 0, 0
    
    idx = -1
    
    for i in range(len(s)):
        hash1 = (hash1 * 26 + ord(s[i])) % PRIME
        hash2 = (ord(s[i]) * power + hash2) % PRIME
        power = (power * 26) % PRIME
        
        if hash1 == hash2: idx = i
            
    return s[idx + 1:][::-1] + s#s[idx + 1:][::-1] + s