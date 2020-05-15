# Nathan Zhu, May 10th, 2020.  Contest.
# Leetcode 1443 | medium | good q
# Category: tree


import collections

def minTime(n, edges, hasApple):
    """
    :type n: int
    :type edges: List[List[int]]
    :type hasApple: List[bool]
    :rtype: int
    """
    graph = collections.defaultdict(list)
    for a, b in edges: graph[a].append(b)
    valid_g = collections.defaultdict(list)

    def helper(curr):
        if curr not in graph: return hasApple[curr]
        ret = hasApple[curr]

        for neigh in graph[curr]:
            status = helper(neigh)
            if status: valid_g[curr].append(neigh)
            ret |= status

        return ret

    helper(0)

    def dfs(curr):
        ret = 0
        for neigh in valid_g[curr]:
            ret += 1
            ret += dfs(neigh)
        ret += 1
        return ret

    return dfs(0) - 1 if 0 in valid_g else 0