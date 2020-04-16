# Nathan Zhu Jan 7th, 2020.  Saturday.
# Leetcode 563 | easy | not that easy
# Category: Binary tree, postorder traversal
# 


def findTilt(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    ret = [0]
    def helper(root):
        if not root: return 0
        left, right = helper(root.left), helper(root.right)
        ret[0] += abs(left - right)
        return left + right + root.val
    helper(root)
    return ret[0]