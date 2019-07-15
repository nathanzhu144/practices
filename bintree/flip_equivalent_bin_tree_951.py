#  Nathan Zhu, American Express Tower, Floor 36th, Sunday June 4:57 pm.  
#  Leetcode 951
#  How to determine if two binary trees are flip equivalent?
#  
#  This is roughly the same problem as whether two binary trees are symmetrical.  If you understand that one, 
#  you should understand that one.
#
#
#  The idea is simple:
# 
#           4               4
#          / \             / \
#         3   5           5  3 
#        
#  Both of these trees are obviously flip equivalent.  At each node, we need to do several things.

def flip_equivalent(root1, root2):
    """
    :type root1: TreeNode
    :type root2: TreeNode
    :rtype: bool
    """
    def helper(root1, root2):
        # If either root1 or root2 are None, both most be None
        if not root1 or not root2: return not root1 and not root2
        # Can be true iff root1 and root2 have same value and  ...
        # 1. the left and right subtrees are flipped
        # 2. the left and right subtrees are equal
        return root1.val == root2.val and ((helper(root1.left, root2.left) and helper(root1.right, root2.right)) or \
                                            (helper(root1.left, root2.right) and helper(root1.right, root2.left)))
    return helper(root1, root2)