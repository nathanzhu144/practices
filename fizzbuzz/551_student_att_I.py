# Nathan Zhu Jan 7th, 2020.  
# Leetcode 551 | easy | easy
# Category: Fizzbuzz
# Done in one pass.

def checkRecord(self, s):
    """
    :type s: str
    :rtype: bool
    """
    ct = s[:2].count('A')
    for i in range(2, len(s)):
        if s[i] == s[i - 1] and s[i] == s[i - 2] and s[i] == 'L' : return False
        if s[i] == 'A': ct += 1
        
    return ct < 2