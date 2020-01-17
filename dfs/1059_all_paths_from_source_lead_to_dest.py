# Nathan Zhu August 28th, 2019 3:25 am
# Leetcode 1059 | medium | medium
# Google- On-Site Interview
# Your interview score of 4.93/10 beats 63% of all users.
# Time Spent: 1 hour 27 minutes 26 seconds
# Time Allotted: 2 hours

# Given the edges of a directed graph, and two nodes source and destination of this graph, 
# determine whether or not all paths starting from source eventually end at destination, that is:
#
# At least one path exists from the source node to the destination node
# If a path exists from the source node to a node with no outgoing edges, then that node is equal to destination.
# The number of possible paths from source to destination is a finite number.
# Return true if and only if all roads from source lead to destination.


def leadsToDestination(n, edges, source, destination):
    """
    :type n: int
    :type edges: List[List[int]]
    :type source: int
    :type destination: int
    :rtype: bool
    """
    graph = collections.defaultdict(list)

    for start, finish in edges:
        graph[start].append(finish)
    
    # Apparently a loop at destination means it doesn't lead to destination.
    if len(graph[destination]) != 0: return False
    
    Q = list([[source, set([source])]])
    while Q:
        nextQ = list()

        for node, visited in Q:
            if node == destination: continue
            if len(graph[node]) == 0: return False

            for neighbor in graph[node]:
                if neighbor in visited: return False
                visited_copy = visited.copy()
                visited_copy.add(neighbor)
                nextQ.append([neighbor, visited_copy])

        Q = nextQ

    return True

# A soln I thought up several months later when I forgot I did this problem.
def leadsToDestinationRecursive(n, edges, source, destination):
    """
    :type n: int
    :type edges: List[List[int]]
    :type source: int
    :type destination: int
    :rtype: bool
    """
    graph = collections.defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        
        
    visited = set()
    def helper(curr, dest):
        # we found it!
        if curr == dest and len(graph[dest]) == 0: 
            return True
        # we got stuck
        if curr != dest and len(graph[curr]) == 0:
            return False
        
        if curr in visited: return False
        visited.add(curr)
        
        for neigh in graph[curr]:
            if not helper(neigh, dest): 
                visited.remove(curr)
                return False
            
        visited.remove(curr)
        return True
    
    return helper(source, destination)