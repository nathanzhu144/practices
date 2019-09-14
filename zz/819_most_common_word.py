# Nathan Zhu September 10th, 2019
# Leetcode 819 | easy | dude this is hard man
# There are so many edge cases in the paragaph like 
# "hello,bye,I am  d dog"

import re
import collections

def mostCommonWord(paragraph, banned):
    """
    :type paragraph: str
    :type banned: List[str]
    :rtype: str
    """
    ban = set(banned)
    # findall in format 
    # \w is equivalent to [a-zA-Z0-9_], and matches all alphanum, but also _
    words = re.findall(r"\w+", paragraph.lower())
    
    
    # most_common returns a list of n of the most common chars in a tuple like (char, count)
    return collections.Counter(w for w in words if w not in ban).most_common(1)[0][0]