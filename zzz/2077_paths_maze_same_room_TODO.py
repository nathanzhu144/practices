
import collections
# TLE approach.
def numberOfPaths_brute_force(n, corridors):
    """
    :type n: int
    :type corridors: List[List[int]]
    :rtype: int
    """
    
    # DS
    # adj list for our graphg
    # Brute force.
    graph = collections.defaultdict(list)
    
    for a, b in corridors:
        graph[a].append(b)
        graph[b].append(a)
        
    paths = set()
    
    # does a BFS to k-depth, returns, number of cycles
    def helper(start, k):     
        q = [[start]]
        
        for i in range(k):
            newq = []
            for path in q:
                node = path[-1]
                for neigh in graph[node]:
                    newq.append(path + [neigh])
            q = newq
        for path in q:
            if path[-1] == start:
                paths.add("".join(map(str, sorted(set(path)))))
    
    for i in range(1, n + 1):
        helper(i, 3)
    return len(paths)