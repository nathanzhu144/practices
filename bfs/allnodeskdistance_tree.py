import collections
#  Nathan Zhu Friday 11:37 pm, Amex tower, 36th floor, June 14th, 2019
#  Leetcode 863
## Helper functions
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def add_node(root, node):
    if not root:
        return node
    if root.val < node.val:
        root.right = add_node(root.right, node)
    else:
        root.left = add_node(root.left, node)
    return root

## Given any arbitrary node in a BST, find all nodes distance k from that node
## We first use a hash table that maps (node) -> [node.parent, node.left, node.right]
#                                 if each of them exist
#
#  
#                                                 5
                                     #          /  \
                                     #         2    6
                                     #        /  \    \
                                     #       1   3    7

#  In this case, the map would contain:
#                       [5] -> [2, 6]
#                       [3] -> [2]
#                       [2] -> [1, 3, 5]
#                       [1] -> [2]
#                       [6] -> [5, 7]
#                       [7] -> [6]

#  After that, we essentially have the info to treat the tree likely a fully-connected graph.
#  We just do a BFS K levels after that.

def distanceK(root, target, K):
    """
    :type root: TreeNode
    :type target: TreeNode
    :type K: int
    :rtype: List[int]
    """
    def make_graph(root, parent, graph):
        if root and parent:
            graph[root].append(parent)
            graph[parent].append(root)
        
        if root.left: make_graph(root.left, root, graph)
        if root.right: make_graph(root.right, root, graph)
            
    if not root:
        return None
    
    temp = root
    graph = collections.defaultdict(list)
    make_graph(root, None, graph)
    
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
                    
        BFS_curr = BFS_next[:]
        BFS_next = list()
        K -= 1
        
    return BFS_curr

if __name__ == "__main__":
    node1 = TreeNode(5)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(6)
    node5 = TreeNode(7)
    node6 = TreeNode(1)

    root = add_node(node1, node2)    #            5
    root = add_node(root, node3)    #          /  \
    root = add_node(root, node4)    #         2    6
    root = add_node(root, node5)    #        /  \    \
    root = add_node(root, node6)    #       1   3    7

    print(distanceK(node1, node2, 1))
