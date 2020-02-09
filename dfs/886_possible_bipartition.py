# Nathan Zhu Sunday Jan 26th, 2019 Foundry lofts 8:55 pm
# Leetcode 886 | medium | medium
# Category: DFS
# Bipartite graph ideas, O(N) time.
# This is a standard question seeing if each subgraph is bipartite
# 

def possibleBipartition(N, dislikes):
    """
    :type N: int
    :type dislikes: List[List[int]]
    :rtype: bool
    """
    graph = collections.defaultdict(list)
    for p, c in dislikes:
        graph[p].append(c)
        graph[c].append(p)
    visited = set()
    
    def is_bipartite(start):
        red, blue = set([start]), set()
        stack = [start]
        while stack:
            curr = stack.pop()
            visited.add(curr)

            for neigh in graph[curr]:
                if curr in red and neigh in red: return False
                if curr in blue and neigh in blue: return False
                if curr in red and neigh not in blue: 
                    blue.add(neigh)
                    stack.append(neigh)
                if curr in blue and neigh not in red: 
                    red.add(neigh)
                    stack.append(neigh)

        return True
                
    for i in range(N + 1):
        if i not in visited and not is_bipartite(i): return False
    return True
        