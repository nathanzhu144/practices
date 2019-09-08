# Nathan Zhu 
# 
# You are given an array of strings words and a string chars.
#
# A string is good if it can be formed by characters from chars
# (each character can only be used once).

# Return the sum of lengths of all good strings in words.

 

# Example 1:

# Input: words = ["cat","bt","hat","tree"], chars = "atach"
# Output: 6
# Explanation: 
# The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.


# Amazon- Online Assessment
# Completed September 4, 2019 4:05 PM
# Your interview score of 8.45/10 beats 87% of all users.
# Time Spent: 12 minutes 35 seconds
# Time Allotted: 1 hour

import collections

def countCharacters(words, chars):
    """
    :type words: List[str]
    :type chars: str
    :rtype: int
    """
    dictionary =  collections.Counter(chars)
    
    ret = 0
    for word in words:
        isGood = True
        used = collections.defaultdict(int)
        for c in word:
            used[c] += 1
            if dictionary[c] - used[c] < 0:
                isGood = False
                break
                
        if isGood: 
            ret += len(word)
                
    return ret