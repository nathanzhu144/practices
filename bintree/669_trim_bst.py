# Nathan Zhu 6:27 pm, 
# Leetcode 669 | easy | I think medium?
# This problem took me ages cause I tried in C++ and ran into a bunch of memory issues lol.
# This is actually a somewhat interesting problem.

def trimBST(root, L, R):
    """
    :type root: TreeNode
    :type L: int
    :type R: int
    :rtype: TreeNode
    """
    def helper(root, L, R):
        if not root: return None
        # We trim this node, but it is possible we don't trim root.right
        if root.val < L: return helper(root.right, L, R)
        # We trim this node, but it is possible we don't trim root.left
        if root.val > R: return helper(root.left, L, R)

        # no trimmings, check left and right subtree
        root.left = helper(root.left, L, R)
        root.right = helper(root.right, L, R)
        return root
    
    return helper(root, L, R)


# Nathan Zhu August 26th, 2019 10:05 pm, Stockton California at buffalo wild wings
# Leetcode 669 | easy | not easy, should be medium I think
# Category: BST
# 
# Done in real-time in a "Microsoft OA", 1 hour time for 2 questions
# Rating was 6.06/10, beating 66% of all users.
# 


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def trimBST(self, root, L, R):
    """
    :type root: TreeNode
    :type L: int
    :type R: int
    :rtype: TreeNode
    """
    def helper(root, L, R):
        if not root: return None
        
        # This node is excluded from the tree
        if root.val < L:
            return helper(root.right, L, R)
        if root.val > R:
            return helper(root.left, L, R)
        
        # We keep this value, no guarantee we keep left or right, so it is possible
        # to exclude this value.
        root.left = helper(root.left, L, R)
        root.right = helper(root.right, L, R)
        return root
    
    return helper(root, L, R)