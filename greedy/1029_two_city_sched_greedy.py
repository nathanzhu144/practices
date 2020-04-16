# Nathan Zhu Jan 5th, 2020.  In SI 106, we have an exam tomorrow!
# Leetcode 1029 | easy | medium
# Category: DP / greedy 
# This is the greedy soln.

def twoCitySchedCost(costs):
    """
    :type costs: List[List[int]]
    :rtype: int
    """
    # greedy solution
    # We sort by the difference in costs between city A and city B
    # We send the first N/2 ppl to city A, and send the last N/2 ppl to city B.
    costs.sort(key = lambda x: x[0] - x[1])
    
    ret = 0
    N = len(costs) // 2
    
    for i in range(N):
        ret += costs[i][0] + costs[N + i][1]
        
    return ret