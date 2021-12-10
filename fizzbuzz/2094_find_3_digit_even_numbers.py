# Nathan Zhu, 12/8/2021, 4:06 am, Stockton, CA
# Leetcode 2094 | easy | annoying, but this solution is actually really elegant
# Category: fizzbuzz
#


import collections
def findEvenNumbers(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    c = collections.Counter(digits)
    ret = []
    
    for i in range(1, 10):
        for j in range(0, 10):
            for k in range(0, 10, 2):
                c[i] -= 1
                c[j] -= 1
                c[k] -= 1
                if c[i] >= 0 and c[j] >= 0 and c[k] >= 0:
                    ret.append(i * 100 + j * 10 + k)
                c[i] += 1
                c[j] += 1
                c[k] += 1
    return ret