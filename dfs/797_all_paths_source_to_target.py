# Nathan Zhu Winter break December 20th, 2019 
# timed mock interview, random company
# Leetcode 797 | easy | EZ
# Category: Graph

# This is the most basic graph problem you can get, lol.  I did it in 3 minutes.


import collections


def allPathsSourceTarget(graph):
    """
    :type graph: List[List[int]]
    :rtype: List[List[int]]
    """
    N_1 = len(graph) - 1
    
    new_graph = collections.defaultdict(list)
    for i in range(len(graph)): new_graph[i] = graph[i]
        
    ret = []
    def helper(graph, currnode, currpath):
        currpath = currpath + [currnode]
        
        if currnode == N_1:
            ret.append(currpath)
        
        for neighbor in new_graph[currnode]:
            helper(graph, neighbor, currpath)
            
    helper(new_graph, 0, [])
    return ret