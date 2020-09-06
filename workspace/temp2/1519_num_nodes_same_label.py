
# /* Nathan Zhu  Saturday July 11th, 2020 Stockton, CA, Weekly contest
# *  Leetcode 1519 | medium | medium
# *  Category: tree
# *  Runtime:  26 * N
# */

import collections


def countSubTrees(n, edges, labels):
    """
    :type n: int
    :type edges: List[List[int]]
    :type labels: str
    :rtype: List[int]
    """
    graph = collections.defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    ret = [0] * n
    visited = set()

    def dfs(node):
        if node in visited: return
        visited.add(node)
        c = collections.Counter()
        c[labels[node]] += 1

        for neigh in graph[node]:
            child_c = dfs(neigh)
            if not child_c: continue
            for k, v in child_c.items():
                c[k] += v

        ret[node] = c[labels[node]]
        return c

    dfs(0)
    return ret
