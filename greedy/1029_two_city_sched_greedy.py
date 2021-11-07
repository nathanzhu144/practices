# Nathan Zhu Jan 5th, 2020.  In SI 106, we have an exam tomorrow!
# Leetcode 1029 | easy | medium
# Category: DP / greedy 
# This is the greedy soln.
#
#         [[10,20],[30,200],[400,50],[30,20]]
#              A      B        C      D
#         [-10, -170, 350, 10]
#         [-170, -10, 10, 350]
#           B    A     D   C
# Idea here is we send all people to city A.
# Then, we have to send N of them to city B.
# How much money could we save?
# If we sent person C to city B, we would save 350 dollars. 
# If we sent person D to city A, we would save 10 dollars.
# 
# Sort from least->most savings, take the half with most savings.

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