# Nathan Zhu, 10:30 pm, Friday June 28th, 2019, on lyft from Chicago O'Hare to Chicago
# Soo, there are 2 ways of solving this problem.
# 1. cool recursive mthod (here)
# 2. level order traversal, return first ele of deque of last level
def findBottomLeftValue(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    # Calculates heights of every node in a binary tree.
    def height(root, node_to_height):
        if not root: return 0
        node_to_height[root] = max(height(root.left, node_to_height), height(root.right, node_to_height)) + 1
        return node_to_height[root]
    
    # Recursively, think of what each nodes needs to do.
    # 
    # 1. If there is a deeper height, bottom tree left value is on that side
    # 2. If there is a tie in height, left side is where bottom tree left value is
    def helper(root, node_to_height):
        if not root: return None
        if not root.left and not root.right: return root.val
        if not root.right: return helper(root.left, node_to_height)
        if not root.left: return helper(root.right, node_to_height)
        if node_to_height[root.left] == node_to_height[root.right]:
            return helper(root.left, node_to_height)
        if node_to_height[root.left] < node_to_height[root.right]:
            return helper(root.right, node_to_height)
        else:
            return helper(root.left, node_to_height)
        
    node_to_height = dict()
    height(root, node_to_height)
    return helper(root, node_to_height)