# Nathan Zhu, Jan 10th, 2020, 10:22 pm, Palmer Commons, Amcult 376 class.  We are talking about Haiti today.
# Leetcode 582 | medium | EZ
# Category: DFS
#
# This is a simple DFS problem.

import collections

def killProcess(pid, ppid, kill):
    """
    :type pid: List[int]
    :type ppid: List[int]
    :type kill: int
    :rtype: List[int]
    """
    graph = collections.defaultdict(list)
    ret = []
    for parent, child in zip(ppid, pid):
        graph[parent].append(child)
        
    def dfs(curr):
        ret.append(curr)
        for child in graph[curr]:
            dfs(child)
            
            
    dfs(kill)
    return ret
        