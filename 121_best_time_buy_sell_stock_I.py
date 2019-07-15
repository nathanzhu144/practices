# Nathan Zhu, July 8th, 2019, 11:28 am, Monday
# Leetcode 121 | easy | not-so-easy
# # 
# For this case, we really have two unknown variables on each day: T[i][1][0] and T[i][1][1], and the recurrence relations say:

# T[i][1][0] = max(T[i-1][1][0], T[i-1][1][1] + prices[i])
# T[i][1][1] = max(T[i-1][1][1], T[i-1][0][0] - prices[i]) = max(T[i-1][1][1], -prices[i])

# where we have taken advantage of the base caseT[i][0][0] = 0 for the second equation.

# It is straightforward to write the O(n) time and O(n) space solution, based on the two equations above. However, if you notice that maximum profits on the i-th day actually only depend on those on the (i-1)-th day, the space can be cut down to O(1). Here is the space-optimized solution:

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    # T[i][k][1] or T[i][k][0]
    # i == ith day, k = number of transactions left, (1 or 0) - 1 is holding stock, 0 is not
    # We have to recurrence relations
    # T[i][1][0] = max(T[i - 1][1][0], T[i - 1][1][1] + prices[i]) 
    # T[i][1][1] = max(T[i - 1][1][1], T[i - 1][0][0] - prices[i]) = max(T[i - 1][1][1], -prices[i]),
    #                                as T[i - 1][0][0] is 0
    #
    # 
    # NOTE: T_i10 >= T_i11, as we can always get a larger or equal profit by selling stock at a profit than holding it
    #                       
    
    T_i10, T_i11 = 0, float("-inf")
    
    for p in prices:
        T_i10 = max(T_i10, T_i11 + p)
        T_i11 = max(T_i11, -p)
        
    return T_i10
    
# This is a less generalized, but easier to understand max_profit funciton
def easier_max_profit(prices):
    if not prices: return 0

    min_so_far = prices[0]
    max_profit = 0

    for i in range(len(prices)):
        min_so_far = min(min_so_far, prices[i])
        max_profit = max(max_profit, prices[i] - min_so_far)

    return max_profit
 