#  
#  

#       5
#      / \
#     4   5
#    / \   \
#   1   1   5
#  Longest univalue path is 2
#
#  NOTE: Longest univalue path may not even go through the root

def longestUnivaluePath(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    # How come we are allowed to access a list globally?
    returned = [0]
    
    def helper(root):
        if not root: return 0

        # left_curr is current univalue path size ending on root.left
        # right_curr is current univalue path ending on root.right
        left_curr = helper(root.left)
        right_curr = helper(root.right)
        
        # we continue left path if left node exists and its value is same as curr node's value
        # we continue right path if right node exists and its value is same as curr node's value
        left = left_curr + 1 if root.left and root.left.val == root.val else 0
        right = right_curr + 1 if root.right and root.right.val == root.val else 0
        
        # it is possible that we form the longest path by doing longest path ending at left +
        #                                 longest path ending at right
        # we check for this possibility here
        # it is also possible that just the left or right path by itself is the longest univalue path
        # we also check for that with this line
        returned[0] = max(returned[0], left + right)

        # we can only include the longest univalue path when we recurse up
        # NOTE: we cannot return left + right
        return max(left, right)
    
    helper(root)
    return returned[0]