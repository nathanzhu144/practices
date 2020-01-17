# Nathan Zhu January 2nd, 2019 Came back from Monterey yesterday.
# Leetcode 168 | easy | not too bad
# Category: Fizzbuzz

import string

def convertToTitle(self, n):
    """
    :type n: int
    :rtype: str
    """
    alphabet = string.ascii_uppercase
    ret = []
    
    # n - 1 is because Excel has weird 1-indexing.
    while n > 0:
        ret.append(alphabet[(n - 1) % 26])
        n = (n - 1) // 26
        
    return "".join(ret[::-1])