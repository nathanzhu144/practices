# Nathan Zhu March 26th, 2020, 12:11 am Foundry Lofts COVID-19
# Leetcode 1129 | medium | medium
# Category: BFS
# 
# 

import collections

def shortestAlternatingPaths(n, red_edges, blue_edges):
    """
    :type n: int
    :type red_edges: List[List[int]]
    :type blue_edges: List[List[int]]
    :rtype: List[int]
    """
    visited = set()
    red_table, blue_table = collections.defaultdict(list), collections.defaultdict(list)
    for a, b in red_edges: red_table[a].append(b)
    for a, b in blue_edges: blue_table[a].append(b)
        
    
    ret = [-1] * n
    q = [("first", 0, 0)]
    
    while q:
        newq = []
        for flag, dist, node in q:
            if ret[node] == -1: ret[node] = dist
            if (flag, node) in visited: continue
            visited.add((flag, node))
            
            if flag != "blue":
                for neigh in blue_table[node]:
                    newq.append(("blue", dist + 1, neigh))
            if flag != "red":
                for neigh in red_table[node]:
                    newq.append(("red", dist + 1, neigh))
        q = newq
        
    return ret