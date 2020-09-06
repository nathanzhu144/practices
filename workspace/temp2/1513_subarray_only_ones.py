# /* Nathan Zhu  Saturday July 11th, 2020 Stockton, CA, Weekly contest
# *  Leetcode 1513 | easy | easy
# *  Category: fizzbuzz
# */


def numSub(s):
    """
    :type s: str
    :rtype: int
    """
    N, MOD = len(s), 10 ** 9 + 7
    ret, curr = 0, 0
    
    for i in range(N):
        if s[i] == '0': curr = 0
        else: curr += 1
        ret += curr
        ret %= MOD
        
    return ret