# Nathan Zhu Dec 26th, 2019 12:18 am, Stockton CA, after christmas
# Leetcode 50 | medium | medium
# 
# Some nasty edge cases, like overflows are avoided bc python.
# doubles in C++ can avoid a lot of these problems

def myPow(x, n):
    """
    :type x: float
    :type n: int
    :rtype: float
    """
    def helper(x, n):
        if n == 0: return 1
        if n == 1: return x
        
        if n < 0: return helper(1 / x, -n)
        elif n % 2 == 1: return x * helper(x, n - 1)
        else: return helper(x * x, n / 2)
    return helper(x, n)