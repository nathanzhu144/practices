# Nathan Zhu 12:04 am, Santa Cruz Sunday December 30th, 2019
# Leetcode 172 | easy | cool one
# Category: number theory
# Q: How many 0s does N! have trailing it?
# I figured a good O(N) soln, but didn't come up with the last insight.
# 

def trailingZeroes(self, n):
    """
    :type n: int
    :rtype: int
    """
    # Idea behind this is simple.
    # If you do prime factorization, 0s come from 10s, which only come from 2s and 5s.
    # There are always more 2s than 5s in a factorial, so we care about number of 5s 
    # in the number.
    #
    # WE can't just do n // 5, as some numbers have more than one 5, like 25.
    # My original soln for this was to do dp, as dp[25] = dp[5] + 1, where
    # the idea behind dp was number of 5s in that number, but this only affords an O(N) runtime
    # amd O(N) space.
    # 
    # It takes another specific insight, that if ther are n // 5 5s, there are n // 25 25s, n // 125 125s and so on,
    # and this can be easily calculated with a loop or recursively, giving us the correct number of 5s.
    # 
    def helper(n, div):
        if n // div == 0: return 0
        return n // div + helper(n, div * 5)
    
    return helper(n , 5)