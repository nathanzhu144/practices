# Nathan Zhu March 19th, 2020 Thursday 10:!5 pm
# Leetcode 250 | medium | medium
# Category: binary tree



def countUnivalSubtrees(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if not root: return 0
    ret = [0]
    def helper(root, val):
        if not root: return True
        
        left = helper(root.left, root.val)
        right = helper(root.right, root.val)
        
        if left and right: ret[0] += 1
            
        return left and right and root.val == val
    helper(root, 0)
    return ret[0]