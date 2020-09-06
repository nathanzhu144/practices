
# /* Nathan Zhu  Saturday July 11th, 2020 Stockton, CA, Weekly contest
# *  Leetcode 1514 | medium | medium
# *  Category: Djikstra shortest path
# */

import collections
import heapq

def maxProbability(n, edges, succProb, start, end):
    """
    :type n: int
    :type edges: List[List[int]]
    :type succProb: List[float]
    :type start: int
    :type end: int
    :rtype: float
    """
    succ = dict()                           # maps pairs to succ probs  (0, 1) -> 0.25
    graph = collections.defaultdict(list)   # maps nodes -> list of other nodes

    for i in range(len(edges)):
        a, b = edges[i]
        succ[(a, b)] = succProb[i]
        succ[(b, a)] = succProb[i]
        graph[a].append(b)
        graph[b].append(a)

    pq = [(-1.0, start)]   # contains pairs of (succ prob, current node)
    visited = set()

    while pq:
        currprob, currnode = heapq.heappop(pq)
        if currnode == end: return currprob * -1
        if currnode in visited: continue
        visited.add(currnode)

        for neigh in graph[currnode]:
            edge = (currnode, neigh)
            heapq.heappush(pq, (currprob * succ[edge], neigh))

    return 0