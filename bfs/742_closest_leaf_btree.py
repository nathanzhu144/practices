# Nathan Zhu Jan 20th, 2019 12:09 pm Potbelly Sandwich shop
# Leetcode 742 | medium | ez
# Category: BFS
#
# This is the same as all nodes distance k, except you return first leaf node.
# Typcial binary tree BFS
# 

import collections

def findClosestLeaf(self, root, k):
    """
    :type root: TreeNode
    :type k: int
    :rtype: int
    """
    graph = collections.defaultdict(list)
    
    # Making tree into a connected graph.
    def connect(curr, parent):
        if not curr: return
        if parent and curr:
            graph[curr].append(parent)
            graph[parent].append(curr)
        connect(curr.left, curr)
        connect(curr.right, curr)
    # finding node of k
    def find(root, k):
        if not root: return None
        if root.val == k: return root
        left = find(root.right, k)
        right = find(root.left, k)
        return left if left else right
        
    connect(root, None)
    curr = find(root, k)
    
    q = collections.deque([curr])
    visited = set([curr])
    
    while q:
        n = q.pop()
        if not n.left and not n.right: return n.val
        
        for neigh in graph[n]:
            if neigh in visited: continue
            visited.add(neigh)
            q.appendleft(neigh)
            
    return 0