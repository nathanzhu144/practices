
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

# def widthOfBinaryTree(root):
#     """
#     :type root: TreeNode
#     :rtype: int
#     """
#     def prune(list_in):
#         left, right = -1,-1
#         for i in range(len(list_in)):
#             if list_in[i] != None:
#                 left = i
#                 break
#         for i in range(len(list_in) - 1, -1, -1):
#             if list_in[i] != None:
#                 right = i
#                 break
#         # If list is all 0s 
#         return list() if left == -1 else list_in[left:right + 1]
            
            
#     def helper(root):
#         BFS_curr, BFS_next = [root], list()
#         max_width = 0
        
#         while BFS_curr:
#             max_width = max(len(BFS_curr), max_width)
#             while BFS_curr:
#                 front = BFS_curr.pop(0)
#                 if not front:
#                     BFS_next.append(None)
#                     BFS_next.append(None)
#                 else:
#                     BFS_next.append(front.left)
#                     BFS_next.append(front.right)
                    
#             BFS_curr = prune(BFS_next[:])
#             BFS_next = list()
        
#         return max_width
    
#     return helper(root)

def widthOfBinaryTree(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    max_width = 0
    
    # leftmost_node_location is a list of integers.
    # leftmost_node_location[level] gives ID of leftmost integer
    def helper(root, id_num, level, leftmost_node_location, max_width):
        if not root: return
        if level >= len(leftmost_node_location): leftmost_node_location.append(id_num)
        max_width = max(max_width, id_num + 1 - leftmost_node_location[level])
        helper(root.left, id_num * 2, level + 1, leftmost_node_location, max_width)
        helper(root.right, id_num * 2 + 1, level + 1, leftmost_node_location, max_width)
            
    helper(root, 1, 0, list(), max_width)
    return max_width

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
    print(widthOfBinaryTree(root))