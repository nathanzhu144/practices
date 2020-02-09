# Nathan Zhu Feb 4th, 2020.  Panera Bread, a good morning.  Kinda tired cuz I woke up at 3:45ish.  
# Leetcode 524 | medium | not bad
# Category: finding a subsequence / string
# Google seems to like this kind of question.

def findLongestWord(s, d):
    """
    :type s: str
    :type d: List[str]
    :rtype: str
    """
    
    d.sort(key = lambda x: (-len(x), x))
    
    for word in d:
        i = 0
        for c in s:
            if i < len(word) and word[i] == c: i += 1
        
        if i == len(word): return word
        
    return ""