# Nathan Zhu Thursday January 2nd, 2019
# Leetcode 787 | medium | not bad
# Category: Dijkstra / PQ, similar to The Maze II
# 
# I'm just happy I had no compilation errors and no logic errors.  Passed everything first try.
# 
import collections
import heapq


def findCheapestPrice(n, flights, src, dst, K):
    """
    :type n: int
    :type flights: List[List[int]]
    :type src: int
    :type dst: int
    :type K: int
    :rtype: int
    """
    max_tickets = K + 1                          # maximum number of tix we can buy
    graph = collections.defaultdict(list)        # graph maps curr_destination to a list of (cost, next_destination) pairs
    pq = [(0, max_tickets, src)]                 # pq is a min heap of (curr_cost, num_tickets_left, curr_node) pairs
    
    for curr_d, next_d, cost in flights:
        graph[curr_d].append((cost, next_d))
    
    while pq:
        cost, tickets, node = heapq.heappop(pq)
        
        if node == dst: return cost                                       # we reached our distination, cost is our minimum cost within k stops
        if tickets == 0: continue                                         # we ran outta tickets goin this way
            
        for next_tick_cost, next_dest in graph[node]:
            heapq.heappush(pq, (cost + next_tick_cost, tickets - 1, next_dest))
        
    return -1