# Nathan Zhu Stockton, CA, COVID-19 Wednesday June 2nd, 2020.
# Leetcode 285 | easy | easy
# Category: Misc tricks
# O(1) with math is hard.  look at the pattern.
def addDigits(self, num):
    """
    :type num: int
    :rtype: int
    """
    
    if num == 0: return 0
    elif num % 9 == 0: return 9
    else: return num % 9