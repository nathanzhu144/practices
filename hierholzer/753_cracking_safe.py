# Nathan Zhu April 9th, 2020 7:22 am, Stockton, CA, COVID-19
# Leetcode 753 | hard | HARDD
# Category: Hierholzer's algorithm

import itertools

def crackSafe(n, k):
    """
    :type n: int
    :type k: int
    :rtype: str
    """
    
#         Why there exists a sequence of k^n+n-1 that contains all permutations? Here comes the proof.
# As shown in the video (on 4:50), if we can find a Euler path that cross all edges, the sequence can be constructed. Remember that a path exists in Euler graph <=> For every node in graph, the in-degree is equal to out-degree. In this case, the node is n-1 digits (let's call it S). The in-degree means all permutations ending with S, which is equal to k. The out-degree means number of all permutations starting with S, which is also k. Thus in-degree = out-degree for each node => the Euler path exist => the sequence can be constructed
    perms = set(map(lambda x: "".join(x), itertools.product(map(str, range(k)),repeat=n)))
    ret = []
    def dfs(node):
        if not perms: return
        for i in range(k):
            nextp = (node + str(i))[1:]
            if nextp in perms:
                perms.remove(nextp)
                dfs(nextp)
                ret.append(str(i))
            
    start = "0" * n
    perms.remove(start)
    dfs(start)
    return start + "".join(ret[::-1])