#  Nathan Zhu Amex Tower 8:21 am, 36th floor, focus room, Thursday June 13th
#  Leetcode 322 | medium | medium
#
#  Suppose your list of coins is [15, 10, 3, 2, 1]
#  
#  Question:
# You are given coins of different denominations and a total amount of money amount. Write a function 
# to compute the fewest number of coins that you need to make up that amount. If that amount of money
#  cannot be made up by any combination of the coins, return -1.
#
#  We have a coin_index that starts at the back.  The idea behind the coin_index is whether to use the 
#  coin pointed to by coin_index.  
#
#                                  [15, 10, 5] amount (20)
#                  /                                                              \
#            [15, 10] amount (20)                                         [15, 10, 5]  amount (15)
#       /             \                                                  /                                 \
#  [15] amount(20)   [15, 10] amount(10)                     [15, 10] amount (15)               [15, 10, 5]  amount(10)
#      ...              /     \                                   /        \                           /               \          
#           [15] amount(10)  [15, 10] amount(0)      [15] amount(15) [15, 10] amount(5)      [15, 10] amount(5)       [15, 10, 5]  amount(5)
#                ...                                                    ...                         ...                        ...
#
#  
def coinChange(scoins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    
    def helper(coins, amount, coin_index, mem):
        key = (amount, coin_index)
        if key in mem:
            return mem[key]
        
        if amount == 0: 
            return 0
        
        if coin_index == -1 or amount < 0:   # 
            return float('inf')
        
        mem[key] = min(helper(coins, amount - coins[coin_index], coin_index, mem) + 1, helper(coins, amount, coin_index - 1, mem))
        return mem[key]
    
    returned = helper(coins, amount, len(coins) - 1, {})
    if returned == float('inf'):
        return -1
    else:
        return returned