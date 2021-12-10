# Nathan Zhu, 12/6/2021, Stockton, CA.  9:30 pm Went to Starbucks and the gym today.
# Leetcode 2065 | hard | not-so-bad, med?
# Insight:
# Maxtime is at most 100, time is at least 10, so each path is at most length 10.
# Each node has at most 4 edges.
# So, there is at most 4^10 states, which is about a million states.
# Iterating through all of them isn't that bad.
# 
# Notes:
# Simple DFS works, each edge has a positive cost, so it will terminate.
# 
# Tried a simple set for backtracking, but this does not work,
# we can visit the node multiple times, and if we visit it twice, 
# when we backtrack, we still have visited it once and cannot remove
# it from the set. That's why the set has a count, too.
#
import collections
def maximalPathQuality(values, edges, maxTime):
    """
    :type values: List[int]
    :type edges: List[List[int]]
    :type maxTime: int
    :rtype: int
    """
    ret = [0]
    
    edge_to_cost = dict()
    adj_matrix = collections.defaultdict(list)
    visited = collections.Counter()
    visited[0] = 1
    
    for a, b, cost in edges:
        edge_to_cost[(a, b)] = cost
        edge_to_cost[(b, a)] = cost
        adj_matrix[a].append(b)
        adj_matrix[b].append(a)
        
        
    def helper(node, curr_cost, curr_value):
        if curr_cost > maxTime:
            return
        
        if node == 0:
            ret[0] = max(ret[0], curr_value)
            
        for neigh in adj_matrix[node]:
            visited[neigh] += 1
            helper(neigh, curr_cost + edge_to_cost[(node, neigh)], curr_value + values[neigh] if visited[neigh] == 1 else curr_value)
            visited[neigh] -= 1
            
    helper(0, 0, 0)
    return ret[0] + values[0]