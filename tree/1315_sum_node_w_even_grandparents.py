# Nathan Zhu May 21st, 2020. 11:59 pm.  Just finished work at Salesforce, day 4.
# Leetcode 1315 | medium | easy
# Category: Binary tree

def sumEvenGrandparent(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    def helper(root, par, grand):
        if not root: return 0
        ret = 0
        if grand and grand.val % 2 == 0: ret += root.val
        return ret + helper(root.left, root, par) + helper(root.right, root, par)
    
    return helper(root, None, None)