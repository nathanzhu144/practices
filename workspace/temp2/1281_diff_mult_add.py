# Nathan Zhu Tuesday July 28th, 2020 8:00 am, Stockton CA.  GOT POSITION #36/14309 for top 0.25% in Weely Contest 199.
#                                                          Last 2 weeks of SF internship.  :O  Met up with Katie, also Dara/Austin yesterday
#                                                          Kaushal has good hummingbird pics.
# Leetcode 1281 | easy | easy
# Category: fizzbuzz
# Runtime: Log10N
# 

def subtractProductAndSum(n):
    tot, prod = 0, 1
    while n > 0:
        prod *= n % 10
        tot += n % 10
        n //= 10
        
    return prod - tot 

def subtractProductAndSumTwo(n):
    """
    :type n: int
    :rtype: int
    """
    arr = map(int, list(str(n)))
    return reduce(lambda x, y: x * y, arr, 1) - sum(arr)