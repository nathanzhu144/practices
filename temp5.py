import collections

def findCircleNum(M):
    """
    :type M: List[List[int]]
    :rtype: int
    """
    # visited which friends?
    # building a graph
    # do a BFS to find each piece of the graph
    
    # Where to handle visited?
    # We don't want to re-visit a node
    # If a node is visited, mark it as such
    def DFS(graph, N, visited):
        for N in visited:
            print(N)
            return
        visited.add(N)
        
        for friends in graph[N]:
            DFS(graph, friends, visited)
    
    # friend -> all friends
    graph = collections.defaultdict(list)
    
    # Building the graph
    for row in range(len(M)):
        for col in range(row + 1, len(M[0])):
            if M[row][col] == 1:
                graph[row].append(col)
                graph[col].append(row)
    
    ret = 0
    visited = set()
    for i in range(len(M)):
        if i not in visited:
            DFS(graph, i, visited)
            ret += 1
    
    return ret

if __name__ == "__main__":
    findCircleNum([[1,1,0],
                    [1,1,0],
                    [0,0,1]])