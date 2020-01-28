# Nathan Zhu Jan 25th, 2020 11:04 am Ugli 3rd floor reading room.  Yash is here too, we doing deep work.
# Leetcode 1326 | hard | yeah kinda hard
# Category: DP / Greedy, but I do DP
# Runtime: N^2

#   [4, 0, 0, 0, 0, 0, 0, 0, 4]
#    0  1  2  3  4  5  6  7  8
# [0 i  i  i  i  i  i  i  i  i]
# [0 1  1  1  1  i  i  i  i  i]
# [0 1  1  1  1  2  2  2  2  2]

def minTaps(self, n, ranges):
    """
    :type n: int
    :type ranges: List[int]
    :rtype: int
    """
    dp = [0] + [float('inf') for i in range(n)]
    
    for i, num in enumerate(ranges):
        left = max(0, i - num)
        right = min(n, num + i)
        
        for j in range(left + 1, right + 1):
            dp[j] = min(dp[j], dp[left] + 1)
    
    return dp[-1] if dp[-1] != float('inf') else -1
        