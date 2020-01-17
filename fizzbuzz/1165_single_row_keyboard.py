# Nathan Zhu January 10th, 2019
# Leetcode 1165 | easy | EZ
# Google Mock onsite 
# Your interview score of 6.50/10 beats 81% of all users.
# Category: Fizzbuzz

def calculateTime(self, keyboard, word):
    """
    :type keyboard: str
    :type word: str
    :rtype: int
    """
    curr = 0
    table = dict()
    ret = 0
    
    for i in range(len(keyboard)):
        table[keyboard[i]] = i
        
    for ch in word:
        ret += abs(curr - table[ch])
        curr = table[ch]
        
    return ret