# Nathan Zhu May 16th, 2020.  5:46 pm, Broke top 200 last week, got exactly 188 briefly, but went down to position 400 because I had 4 stupid mistakes. 
# Leetocde 1402 | hard | not bad
# Category: DP / Greedy
# This is an N^2 DP problem, but has a more elegant greedy approach.
# I do it with DP here.
#
# Idea:
# We sort all dishes by smallest to greatest.
# We take a dish or do not take a dish

def maxSatisfaction(arr):
    """
    :type satisfaction: List[int]
    :rtype: int
    """
    
    N = len(arr)
    dp = dict()
    arr.sort()  # smallest to greatest
    
    def helper(i, num_dishes):
        if i == N: return 0
        key = (i, num_dishes)
        if key in dp: return dp[key]
        
        dp[key] = max(arr[i] * num_dishes + helper(i + 1, num_dishes + 1), helper(i + 1, num_dishes))
        return dp[key]
    
    return helper(0, 1)