# Nathan Zhu 11:39 pm Think im coming down with a cold.
# Leetcode 424 | medium | med
# Category: Sliding window
# Intuition: counter contains all chars in our window, we take advantage of most_common function of counter
#            to figure out which character to change other chars to.

import collections

def characterReplacement(s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    ret = 0
    left = 0
    c = collections.Counter([])
    for right in range(len(s)):
        c[s[right]] += 1
        
        # Target is character we are trying to change other chars to
        target_count = c.most_common(1)[0][1]
        
        while right - left + 1 - target_count > k:
            c[s[left]] -= 1
            left += 1
            
        ret = max(ret, right - left + 1)
    
    return ret
        
if __name__ == "__main__":
    characterReplacement("AGADABBBABADA", 1)