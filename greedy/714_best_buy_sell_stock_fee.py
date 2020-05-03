# Nathan Zhu April 12th, 2020. 
# Leetcode 714 | medium | kinda tricky
# Category: Greedy
# 
# The barrier behind a greedy approach is that if we buy/sell too many times, we can get a suboptimal profit.
# 
# There are two major types of situations:
#
# 1. We could've sold at a higher price the next day.
# 2. The price tomorrow fluctuates in between (highest price - fee) and highest price
#    In this case, it is unclear whether we should've sold yet, and this will be determined
#    once it makes a new high or goes below (highest price - fee)
# 3. The price goes below (highest price - fee) in which case we should've sold yesterday.
#
# We can categorize 1 & 2 in the same category as an upward trend.  We move our sell price everytime we move to a new high.  
# Ex. 
# arr = [1, 4, 5, 4, 8] fee == 2
# 
#    i = 0 minimum = 1, profit = 0 
#    i = 1 minimum = (4 - 2) = 2, profit = 0 + 4 - 2 - 1 = 1   (up to this point, we are in an uptrend, we mark new profit as 1)
#    i = 2 minimum = (5 - 2) = 3, profit = 1 + 5 - 2 - 2 = 2   (up ot this point, we are in an uptrend, we move our sell from yesterday to today, with a profit of 2)
#    i = 3 minimum = 3.  It is not true that 5 - 3 > 2.        We keep our sell to yesterday.
#    i = 4 minimum = (8 - 2) = 6, profit = 2 + 8 - 2 - 3 = 5   (we are in uptrend still, move our sell from i = 2 to i = 4)
#  
# Note that if we ever go in a downtrend, we definitely know we can "lock in" the last sell in an uptrend.
# 
# 
# 
#  
def maxProfit(prices, fee):
    """
    :type prices: List[int]
    :type fee: int
    :rtype: int
    """
    N = len(prices)
    ret = 0
    min_price = prices[0]
    
    for i in range(1, N):
        currp = prices[i]
        if currp < min_price:
            min_price = currp
            
        if currp - fee > min_price:
            ret += (currp - min_price - fee)
            min_price = currp - fee
            
    return ret