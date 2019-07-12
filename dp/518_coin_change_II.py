#  Nathan Zhu Monday July 1st, 7:25 pm.  
#  Coin Change II, Leetcode 322 | Leetcode medium | I think easy
#
#  You are given coins of different denominations and a total amount of money
#   amount. Write a function to compute the fewest number of coins that you need 
#   to make up that amount. If that amount of money cannot be made up by any 
#   combination of the coins, return -1.
#
#  We can memoize, as we re-solve the subproblem: making "amount" with first "index" coins.
#


def change(self, amount, coins):
    """
    :type amount: int
    :type coins: List[int]
    :rtype: int
    """
    def helper(coins, index, amount, mem):
        key = (index, amount)
        if key in mem: return mem[key]

        if index < 0 or amount < 0: return 0
        if amount == 0: return 1
        mem[key] = helper(coins, index - 1, amount, mem) + \
            helper(coins, index, amount - coins[index], mem)
        return mem[key]
    
    if amount == 0: return 1
    if not coins: return 0
    return helper(coins, len(coins) - 1, amount, dict())
            
            