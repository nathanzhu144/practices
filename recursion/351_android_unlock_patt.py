# Nathan Zhu August 30th, 10:55 pm 
# Leetcode 351 | medium | hard
# Category: DFS
# 
# Google- On-Site Interview
# Your interview score of 5.54/10 beats 87% of all users.
# Time Spent: 1 hour 51 minutes 22 seconds
# Time Allotted: 2 hours


# Given an Android 3x3 key lock screen and two integers m and n, where 1 ≤ m ≤ n ≤ 9, count the total number of
# unlock patterns of the Android lock screen, which consist of minimum of m keys and maximum n keys.

# Rules for a valid pattern:
# Each pattern must connect at least m keys and at most n keys.
# All the keys must be distinct.
# If the line connecting two consecutive keys in the pattern passes through any other keys, the other keys must 
# have previously selected in the pattern. No jumps through non selected key is allowed.
# The order of keys used matters.


def numberOfPatterns(self, m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    graph = dict()
    
    graph[(1,7)] = 4
    graph[(1,3)] = 2

    graph[(1,9)] = 5        
    graph[(2,8)] = 5
    
    graph[(3,7)] = 5
    graph[(3,9)] = 6
    graph[(4,6)] = 5
    graph[(7,9)] = 8
    

    self.ret = 0
    
    def helper(curr, used):
        if len(used) >= m: self.ret += 1
        if len(used) == n: return
        
        for i in range(1, 10):
            if i not in used:
                
                move = (min(curr, i), max(curr, i))
                if move not in graph or graph[move] in used:
                    helper(i, used + [i])
                    
    for i in range(1, 10):
        helper(i, [i])
    
    return self.ret