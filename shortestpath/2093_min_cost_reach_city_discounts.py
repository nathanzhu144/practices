# Nathan Zhu, 12/7/2021, 4:41 pm, panera bread, stockton, CA
# Leetcode 2093  | medium | cool problem
# Category: Dijkstra
#
# Dijkstra with pruning,
# If we reach a node again with equal or fewer discounts,
# it is a dead end and can be pruned.
# All edges are positive, so we can use Dijkstra

import heapq
import collections

def minimumCost(n, highways, discounts):
    """
    :type n: int
    :type highways: List[List[int]]
    :type discounts: int
    :rtype: int
    """
    pq = [(0, 0, discounts)]
    graph = collections.defaultdict(list)
    visited = dict()
    cost = dict()
    
    for a, b, dist in highways:
        graph[a].append(b)
        graph[b].append(a)
        cost[(a, b)] = dist
        cost[(b, a)] = dist
    
    while pq:
        curr_cost, node, curr_disc = heapq.heappop(pq)
        
        # Because of how djikstra works, when we reach this node the first time,
        # we will reach there with the lowest cost.  However, we may reach this node
        # again with a highest cost, but more discount tickets, which can lead to a 
        # more optimal soln at the end.  If we ever come back to this node with the same or 
        # fewer discounts, the soln is not optimal.
        if node in visited and curr_disc <= visited[node]: continue
        visited[node] = curr_disc
        
        if node == n - 1:
            return curr_cost
        for neigh in graph[node]:
            if curr_disc > 0:
                heapq.heappush(pq, (cost[(node, neigh)] // 2 + curr_cost, neigh, curr_disc - 1))
            heapq.heappush(pq, (cost[(node, neigh)] + curr_cost, neigh, curr_disc))
    # no soln
    return -1