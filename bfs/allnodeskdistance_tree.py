def distanceK(self, root, target, K):
    """
    :type root: TreeNode
    :type target: TreeNode
    :type K: int
    :rtype: List[int]
    """
    def try_append(graph, key, val):
        if key in graph:
            graph[key].append(val)
        else:
            graph[key] = [val]

    def make_graph(root, graph):
        if not root:
            return

        if root.left:
            try_append(graph, root.left, root)
            try_append(graph, root, root.left)
            make_graph(root.left, graph)
        if root.right:
            try_append(graph, root.right, root)
            try_append(graph, root, root.right)
            make_graph(root.right, graph)
    
    temp = root
    graph = dict()
    make_graph(temp, graph)
    
    BFS_curr = [target]
    BFS_next = []
    visited = set()
    
    while K > 0 and BFS_curr:
        while BFS_curr:
            front = BFS_curr.pop(0)
            
            if front in visited:
                continue
            visited.add(front)
            
            for node in graph[front]:
                if node not in visited:
                    BFS_next.append(node)
                    
        BFS_curr = BFS_curr[:]
        BFS_next = []
        K -= 1
        
    return BFS_curr