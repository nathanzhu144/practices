#  Nathan Zhu 12:23 am Thursday July 11th, 2019  New York Subway
#  Leetcode 343 | medium | medium
#  Category: DP, math? 
#            there's a way Joe McCann at Amex told me that involved math and limits,
#            if you greedily choose 3s until you can only use 2s, you get optimal ans, 
#            can prove with limit
#  Runtime: Think N^2, space O(N)
#  There are a maximum of n subproblems, however, the for loop can range over n/2 items.  So, is runtime
#  O(n^2)
#  
#  Yo, I cracked this one in the subway, C line.   I was so proud of myself.
#
#  Given a positive integer n, break it into the sum of at least two positive integers 
# and maximize the product of those integers. Return the maximum product you can get.


# Let's talk about the subproblems here.
# Suppose we know integer_break(n) is composed of integer_break(j) * integer_break(k), where 2 <= k < n and 2 <= j < n

def integer_break(n):
    def helper(n, mem):
        if n < 2: return 0
        if n == 2: return 1
        if n in mem: return mem[n]

        max_prod = 0
        # Using i and n - i, we can generate all the pairs from ...
        # Suppose n == 6:
        # 1 5, 2 4, 3 3,
        # Suppose n == 7:
        # 1 5, 2 4, 3 3,
        for i in range(1, n // 2 + 1):
            # so, I made a mistake in the recurrence relationship earlier
            # I had:
            #   max_prod = max(max_prod, (n - i) * i, helper(n - i, mem) * helper(i, mem))
            # The idea is that either we don't break it further and just multiply (n - i) * i 
            #                         OR break it further helper(n - i, mem) * helper(i, mem)
            #   
            # The problem here is that it is possible we break down (n - i), but don't break n.
            # or we can further break down n, but not break (n - i). Breaking down one does not affect
            # breaking down the other.  They are not mutually exclusive.
            #
            # So, instead we take the max of max((n - i), helper(n - i, mem)) and of the other one too.
            max_prod = max(max_prod, max((n - i), helper(n - i, mem)) * max(i, helper(i, mem)))
        mem[n] = max_prod
        return max_prod
    return helper(n, dict())

if __name__ == "__main__":
    print(integer_break(8))