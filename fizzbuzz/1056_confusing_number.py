# Nathan Zhu Jan 31st, 2019 Foundry Lofts 8:00 pm, about to go to Bdubs with Hershal on a Friday evening
# Leetcode 1056 | easy | easy
# Category: Fizzbuzz
#


def confusingNumber(self, N):
    """
    :type N: int
    :rtype: bool
    """
    n = str(N)
    table = {"6":"9", "9":"6", "8":"8", "0":"0","1":"1"}
    
    newn = []
    for ch in n:
        if ch not in table: return False
        newn.append(table[ch])
        
    return not "".join(newn[::-1]) == n
        
            