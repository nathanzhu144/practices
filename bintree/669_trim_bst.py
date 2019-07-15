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