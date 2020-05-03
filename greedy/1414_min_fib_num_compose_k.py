# Nathan Zhu April 18th, 2020. 
# Leetcode 1416 | medium | O(N) is hard to prove
# Category: DP / Greedy
# Encountered this in a biweekly contest. I timed out, but was close.  Didn't think of greedy soln.
def findMinFibonacciNumbers(k):
    """
    :type k: int
    :rtype: int
    """
    # this question I met a biweekly contest, and I performed 3 different N^2
    # approaches, and didn't see the O(N) approach.
    #
    # First, I did a DFS with memoization.  Then, I did a bottom-up dp with memo
    # Then, I did a BFS with visited set.  All timed out.
    #
    # We can do a greedy O(N) solution.
    # Intuition is that the optimal solution works similarly to greedy coin chanage
    # with denominations [1, 1, 2, 3, 5].  Since each bigger coin is a linear 
    # combination of previous coins, and the number of smaller coins it takes to 
    # represent a bigger coin is monotonically increasing, it is always more optimal to 
    # choose a bigger coin than a smaller one.
    #
    # Ex. [1, 1, 2, 3, 5] -> [1 x 1, 1 x 1, 2 x 1, 3 x 1, 5 x 1]
    
    fib = [1, 1]
    while fib[-1] <= k:
        fib.append(fib[-1] + fib[-2])

    ret = 0
    for i in range(len(fib) - 1, -1, -1):
        ret += (k // fib[i])
        k %= fib[i]
    return ret
