# Nathan Zhu, June 23rd, 2019, American Express Tower, New York, NY
# Longest diameter in binary tree.

#  NOTE: Longest diameter path may not even go through the root
#  Similar problems:Leetcode 687, longest univalue path

def diameterOfBinaryTree(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    returned = [0]
    def helper(root):
        if not root: return 0

        # left_curr is longest path leading up to root.left
        # right_curr is longest path leading up to root.right
        left_curr = helper(root.left)
        right_curr = helper(root.right)
        
        # We only add 1 to left path if root has a left
        # We only add 1 to right path if root has a right
        left = left_curr + 1 if root.left else 0
        right = right_curr + 1 if root.right else 0
        
        # At any point, we can create a complete diameter by adding left and right paths
        # ending at this node.  We check if doing so gives up a longest path
        returned[0] = max(returned[0], left + right)

        # We return longest path ending at root
        # NOTE: We cannot use left + right...
        return max(left, right)
    
    helper(root)
    return returned[0]