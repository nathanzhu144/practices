# Nathan Zhu Completed September 6, 2019 5:43 PM
# Leetcode 88 | easy | EZ
# Category: Binary tree
#
# Microsoft- Online Assessment
# Your interview score of 5.90/10 beats 58% of all users.
# 
# Given a binary search tree and a node in it, find 
# the in-order successor of that node in the BST.

# The successor of a node p is the node with the smallest key 
# greater than p.val.

def inorderSuccessor(root, p):
    """
    :type root: TreeNode
    :type p: TreeNode
    :rtype: TreeNode
    """
    def helper(root, p):
        if not root: return None
        
        if root.val <= p.val: return helper(root.right, p)
        else:
            left = helper(root.left, p)
            
            return left if left else root
        
    return helper(root, p)