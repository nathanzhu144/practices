# Nathan Zhu April 4th, 2020.  Stockton, CA, COVID-19.  Salesforce internship starting in 2 weeks, got an A+ in 376, aced that binary search question
#                              in 376 final.  What a blast!
# Leetcode 671 | Easy | easy
# Category: btree

def findSecondMinimumValue(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    ret = [float('inf')]
    
    def helper(root, val):
        if not root: return
        if val != root.val:
            ret[0] = min(ret[0], root.val)
            return
        helper(root.left, val)
        helper(root.right, val)
        
    helper(root, root.val)
    return ret[0] if ret[0] != float('inf') else -1