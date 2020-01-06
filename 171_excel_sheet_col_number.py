# Nathan Zhu January 2nd, 2019 Got back from Santa Cruz point lobos yesterday.
# Leetcode 171 | easy | EZ
# Category: Fizzbuzz
#
# Basic base conversion ideas.
import string
def titleToNumber(s):
    """
    :type s: str
    :rtype: int
    """
    ret = 0
    
    alphabet = string.ascii_uppercase
    table = dict()
    for i, ch in enumerate(alphabet):
        table[ch] = i + 1
        
    multiplier = 1
    st = list(s)
    while st:
        ret += table[st.pop()] * multiplier
        multiplier *= 26
        
    return ret