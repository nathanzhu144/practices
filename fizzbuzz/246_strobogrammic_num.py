# Nathan Zhu Jan 13th, 2019 1:48 pm Volkovitch 376 lecture, they're talking about proving Euclid's algo is logN
# Leetcode 246 | easy | EZ
# Category: Fizzbuzz
# 



def isStrobogrammatic(self, num):
    """
    :type num: str
    :rtype: bool
    """
    # 6 9 -> 9 6
    
    # 0, 1, 6->9, 9->6, 8
    table = {"0":"0", "1":"1", "9":"6", "6":"9", "8":"8"}
    
    for c1, c2 in zip(num, num[::-1]):
        if c1 not in table or table[c1] != c2: return False
        
    return True