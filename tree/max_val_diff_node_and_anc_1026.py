#  Nathan Zhu, Amex Tower, New York, Sunday June 23rd, 2019 36th floor
#   So this is a classic recursion problem.
#
#  We want to find the maximum value difference between any node and its ancestor.
#
#  We basically pass the max_val of a node so far, and min_val of a node so far.
#  when we get to a null, we return max_val - min_val, as that's the biggest difference
#  we can get down that branch.


def maxAncestorDiff(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    def helper(root, min_val, max_val):
        if not root: return max_val - min_val
        min_val = min(root.val, min_val)
        max_val = max(root.val, max_val)
        return max(helper(root.left, min_val, max_val), helper(root.right, min_val, max_val))
    
    return helper(root, root.val, root.val)