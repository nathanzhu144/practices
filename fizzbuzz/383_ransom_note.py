# Nathan Zhu Jan 13th, 2019 11:42 am 376 Lecture
# Leetcode 383 | easy | EZ
# Category: Fizzbuzz


def canConstruct(ransomNote, magazine):
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """
    c = collections.Counter(magazine)
    
    for ch in ransomNote:
        c[ch] -= 1
        if c[ch] == -1: return False
        
    return True