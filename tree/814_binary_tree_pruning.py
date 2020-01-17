# Nathan Zhu 10:13 pm, Friday June 28th, 2019, on car from Chicago O'Hare to Chicago
# Leetcode 814 | medium | I think med
# This problem has a similar logic to LCA.

# For this problem we prune all subtrees not containing 1.
def pruneTree(root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    def helper(root):
        if not root: return None
        
        # we don't know yet if we want to prune left and right 
        # of root yet.  See LCA problem for similar logic.
        root.left = helper(root.left)
        root.right = helper(root.right)
        
        # If left and right don't exist, they either have been pruned 
        # or never existed in first place.  So, we prune this root if
        # this root isn't one.
        if not root.left and not root.right and root.val != 1:
            return None
        else:
            return root
        
    return helper(root)