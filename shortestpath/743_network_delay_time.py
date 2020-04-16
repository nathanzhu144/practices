# Nathan Zhu Jan 7th, 2020.  
# Leetcode 743 | medium | medium
# Category: Djikstra / greedy


import heapq
import collections



def networkDelayTime(times, N, K):
    """
    :type times: List[List[int]]
    :type N: int
    :type K: int
    :rtype: int
    """
    graph = collections.defaultdict(list)
    
    for a, b, dist in times:
        graph[a].append((b, dist))
        
    nodes = set(range(1, N + 1))
    visited = set()
    
    pq = [(0, K)]
    
    while pq:
        dist, curr = heapq.heappop(pq)
        if curr in nodes: nodes.remove(curr)
        if not nodes: return dist
        if curr in visited: continue
        visited.add(curr)
        
        for neigh, nextdist in graph[curr]:
            heapq.heappush(pq, (nextdist + dist, neigh))
            
    return -1