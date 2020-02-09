# Nathan Zhu Jan 31st, 2020 
# Leetcode 938 | easy | good question
# Category: BST
# I was so stupid when I did this before, didn't prune branches.  You should prune branches.

def rangeSumBST(root, L, R):
    """
    :type root: TreeNode
    :type L: int
    :type R: int
    :rtype: int
    """
    
    def helper(root, L, R):
        if not root: return 0
        
        if L <= root.val <= R: 
            return root.val + helper(root.left, L, R) + helper(root.right, L, R)
        elif root.val < L:
            return helper(root.right, L, R)
        elif root.val > R:
            return helper(root.left, L, R)
        
        # Never should get here.
        else: return float('-inf')
    return helper(root, L, R)