

def is_graph_bipartite(graph):
    # node -> color
    color = 0
    visited = dict()
    BFS = collections.deque([0])
    while BFS:
        BFS_next = list()
        for node in BFS:
            if node in visited:
                if visited[node] != color: return False
            else:
                visited[node] = color
                # adding on neighbors of node to next
                BFS_next += graph[node]

        color = not color
        BFS = BFS_next[:]

    return True