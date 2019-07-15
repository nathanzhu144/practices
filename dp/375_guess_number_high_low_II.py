# Nathan Zhu, Amex Building, July 14th, 2019, 7:04 pm, 200 Vessey Street
# Leetcode 375 | medium | medium
# Category: DP, Minimax
# Similar problems: VERY SIMILAR TO SUPER EGG DROP
#
# Description:
# We are playing the Guess Game. The game is as follows:
# 
# I pick a number from 1 to n. You have to guess which number I picked.
# Every time you guess wrong, I'll tell you whether the number
# I picked is higher or lower.
# a particular number x, and you guess wrong, you pay $x. You win
# the game when you guess the number I picked


# The logic here is exactly that of an easier super egg drop, with a slight difference
# when you break problem down, floor number matters.
def money_amount(n):
    def helper(low, high, mem):
        if low >= high: return 0
        key = (low, high)              # we memoize based off of (low, high)
        if key in mem: return mem[key]
        
        ret = float('inf')
        # we want to find the minimum i-value we can pick, to minimize the worst case scenario
        for i in range(low, high + 1):
            ret = min(ret, i + max(helper(low, i - 1, mem), helper(i + 1, high, mem)))
            
        mem[key] = ret
        return ret
        
    return helper(1, n, dict())