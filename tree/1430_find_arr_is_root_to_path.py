# Nathan Zhu May 2nd, 2020. Finidhed 376 exam 4 days ago.  Just got top 400 in a leetcode weekly contest 182!
# Leetcode 1430 | medium | medium
# Category: binary tree
def isValidSequence(root, arr):
    """
    :type root: TreeNode
    :type arr: List[int]
    :rtype: bool
    """
    def is_leaf(root):
        return not root.left and not root.right
    
    def helper(root, i):
        if not root: return False
        if is_leaf(root) or i == len(arr) - 1:
            return is_leaf(root) and i == len(arr) - 1 and root.val == arr[-1]
        
        if root.val != arr[i]: return False
        else: 
            return helper(root.left, i + 1) or helper(root.right, i + 1)
    
    return helper(root, 0)