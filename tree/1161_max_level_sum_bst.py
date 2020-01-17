# Nathan Zhu January 10th, 2019
# Leetcode 1161 | easy | EZ
# Google Mock onsite 
# Your interview score of 6.50/10 beats 81% of all users.
# Category: Binary Tree

def maxLevelSum(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    table = collections.defaultdict(int)
    
    def helper(root, level):
        if not root: return
        table[level] += root.val
        
        helper(root.left, level + 1)
        helper(root.right, level + 1)
        
    helper(root, 1)
    return max(table, key=table.get)