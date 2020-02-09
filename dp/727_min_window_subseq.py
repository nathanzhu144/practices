# Nathan Zhu Jan 20th, 2019 11:24 am, Potbelly Sandwich Shop, State Street, Watched 1917 last night with Hershal.
# Leetcode 727 | hard | hard AFFF lmao
# Category: DP

import collections

def minWindow(S, T):
    m, n = len(S), len(T)
    start, length = -1, float('inf')
    dp = [-1 for i in range(n)]
    
    table = collections.defaultdict(list)
    for idx, c in enumerate(T):
        table[c].append(idx)
        
    for idx, c in enumerate(S):
        if c not in table: continue  
        # We go from the back idx of character c to front occur of idx c
        for i in table[c][::-1]:
            # When i hits 0, we start a new subseq starting with "idx", which idx we are at in the string S right now.
            if i == 0: dp[0] = idx
            # dp[i] is equal to index of dp[i - 1], as:
            # 1. dp[i - 1] == -1, then dp[i] is also unreachable and is thus -1
            # 2. dp[i - 1] == A, where A is a pos integer.  This means there's a subseq starting with idx A going up to dp[i - 1]
            #    Since we found the next character, we can further extend the subseq with the same starting index.
            else: dp[i] = dp[i - 1]
            
            # We have found a substring that contains our subseq (i == n - 1 and dp[i] >= 0) and 
            # this substring is shorter than the previous one (idx - dp[i] + 1 < length)
            if i == n - 1 and dp[i] >= 0 and idx - dp[i] + 1 < length:
                start = dp[i]
                length = idx - dp[i] + 1
    
    if dp[-1] == -1: return ""
    else: return S[start : start + length]


print(minWindow("fgrqsqsnodwmxzkzxwqegkndaa", "fnok"))