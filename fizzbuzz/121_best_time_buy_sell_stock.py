# Nathan Zhu March 23rd, 2020 11:07 pm Foundry Lofts, Covid-19
# Leetcode 121 | easy | not bad
# Category: Fizzbuzz

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    ret = 0
    if not prices: return 0
    
    min_price = prices[0]
    
    for price in prices[1:]:
        min_price = min(price, min_price)
        ret = max(ret, price - min_price)
    return ret