# Nathan Zhu 10:03 pm January 3rd, 2019 I think I am coming down with a cold.
# Leetcode 567 | medium | easy
# classic sliding window

import collections

# We want to check if s2 contains the permutation of s1.  
def checkInclusion(s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: bool
    """
    
    # abcd 
    #    ^
    #    R
    
    left, right = 0, 0
    c = collections.Counter(s1)
    num_chars_left = len(set(s1))
    
    while right < len(s2):
        c[s2[right]] -= 1
        if c[s2[right]] == 0: num_chars_left -= 1
        right += 1
        
        if right - left == len(s1) + 1:
            c[s2[left]] += 1
            if c[s2[left]] == 1: num_chars_left += 1
            left += 1
                
        if right - left == len(s1) and num_chars_left == 0: return True
    return False