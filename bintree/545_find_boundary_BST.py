# Nathan Zhu Winter break December 20th, 2019 
# timed mock interview, random company
# Leetcode 545 | medium | hard
# Category: BST / misctricks
# 
# Bro this one is hard...
# I actually mis-understood the directions that left boundary is this:
#
# Left boundary is defined as the path from root to the left-most node. 
# Right boundary is defined as the path from root to the right-most node. 
# If the root doesn't have left subtree or right subtree, then the root 
# itself is left boundary or right boundary. Note this definition only 
# applies to the input binary tree, and not applies to any subtrees.
#
#      7
#     /
#    2 
#     \
#     3
#     /
#    10
#   /
#  9
# 9 is leftmost node in binary tree, but 2 is left boundary. 
#

# The idea is to pass the markers of left and right boundaries down, and identify
# leaves by a node lacking both a left and right node.

def boundaryOfBinaryTree(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if not root: return []
    ret = [root.val]
    
    def helper(root, is_left, is_right):
        if not root: return
        
        # This is a left boundary
        if is_left or (root.left == None and root.right == None):
            ret.append(root.val)
        
        # If we move left (and there exists a right node), we have to abandon the right flag
        # If we move right (and there exists a left node), we have to abandon the left flag
        if root.left and root.right:
            helper(root.left, is_left, False)
            helper(root.right, False, is_right)
            
        else:
            helper(root.left, is_left, is_right)
            helper(root.right, is_left, is_right)
            
        if (root.left or root.right) and is_right:
            ret.append(root.val)
            
    helper(root.left, True, False)
    helper(root.right, False, True)
    
    return ret