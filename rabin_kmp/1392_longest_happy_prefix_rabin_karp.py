# Nathan Zhy May 19th, 2020 2nd day of work at Salesforce.  
# Leetcode 1392 | hard | hard if you don't know KMP or rabin karp
# Category: Rabin-karp
# This solution seems to time out on leetcode, but seems to be correct.
#

import collections

def longestPrefix(s):
    """
    :type s: str
    :rtype: str
    """
    MOD = 10 ** 7
    table = collections.defaultdict(list)
    ret = 0
    N = len(s)
    
    shash = 0
    for i, ch in enumerate(s):
        shash = (27 * shash + (ord(ch) - ord('a') + 1)) % MOD
        table[shash].append(s[:i + 1])
        
    shash = 0
    power = 0
    for i, ch in enumerate(s[::-1]):
        shash = ((27 ** power) * (ord(ch) - ord('a') + 1) + shash) % MOD
        power += 1
        
        # collision resolution
        if shash in table:
            for forward_string in table[shash]:
                if forward_string == s: break
                if forward_string == s[N - i - 1:]:
                    ret = max(len(forward_string), ret)
                    
    return s[:ret]
                    