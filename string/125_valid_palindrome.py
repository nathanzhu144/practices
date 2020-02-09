# Nathan zhu Saturday January 10:05 pm Foundry Lofts aboutta go to bed
# Leetcode 125 | easy | EZ
# Category: fizzbuzz


def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    left, right = 0, len(s) - 1
    
    while left < right:
        while left < right and not s[left].isalnum(): left += 1
        while left < right and not s[right].isalnum(): right -= 1
        
        if s[right].lower() != s[left].lower(): return False
        left += 1
        right -= 1
        
    return True
        