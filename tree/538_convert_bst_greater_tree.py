#  Nathan Zhu, Monday 3:13 pm, Amex Building 36th floor
#  Leetcode 538 | leetcode easy | I think medium
#  The idea here is that a regular pre-order traversal goes in order from smallest to
#  greatest.  What if we go from the largest to smallest by modifying a in-order traversal?

def convert_greater(root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    def helper(root, root_sum_so_far):
        if not root: return root_sum_so_far
        
        # sum of all nodes on right
        right = helper(root.right, root_sum_so_far)
        # add sum of all nodes on right
        root.val += right
        # pass sum of everything on right to everything on left
        left = helper(root.left, root.val)
        return left
        
    helper(root, 0)
    return root