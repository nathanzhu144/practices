# Nathan Zhu August 29th, 2019 12:58 am
# Leetcode 399 | medium | pretty hard lol
# Category: BFS
# 
# Google on-site interview
# Your interview score of 6.04/10 beats 87% of all users.
# Time Spent: 1 hour 30 minutes 12 seconds
# Time Allotted: 2 hours


# equations = [ ["a", "b"], ["b", "c"] ],
# values = [2.0, 3.0],
# queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 

# Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number
# (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.



def calcEquation(self, equations, values, queries):
    """
    :type equations: List[List[str]]
    :type values: List[float]
    :type queries: List[List[str]]
    :rtype: List[float]
    """
    graph = collections.defaultdict(list)
    
    # Evaluate is a map from (a, b) -> val of a / b
    evaluate = dict()
    for i in range(len(equations)):
        top, bottom = equations[i]
        graph[top].append(bottom)
        graph[bottom].append(top)
        
        evaluate[(top, bottom)] = values[i]
        evaluate[(bottom, top)] = 1 / float(values[i])
        
    # Here we do a BFS and calculate cost of path.
    # Returns query value, -1 if query doesn't exist.
    def handlequery(query, graph, evaluate):
        start, end = query[0], query[1]
        if start not in graph or end not in graph: return -1
        
        # I assume a visited set is a good idea,
        # Reasoning here is that if we ever go back to
        # a node, we have two terms in the equation we can
        # multiply to become 1, and we have formed a longer
        # path than we need to.  
        # NOTE: [(currnode, currcost)]
        q = [(start, 1)]
        visited = set()
        while q:
            nextq = list()
            for node, cost in q:
                if node == end: return cost
                
                visited.add(node)
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        nextq.append((neighbor, cost * evaluate[(node, neighbor)]))
            q = nextq
        return -1
    
    return [handlequery(q, graph, evaluate) for q in queries]