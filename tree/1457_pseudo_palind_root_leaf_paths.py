# Nahan Zhu May 23rd, 2020 saturday, weekly contest
# Leetcode 1457 | medium | loved this question
# Category: binary tree

import collections
def pseudoPalindromicPaths (self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    def helper(root, table, num_odds):
        if not root: return
        table[root.val] += 1
        if table[root.val] % 2 == 1: num_odds += 1
        else: num_odds -= 1
        if num_odds <= 1 and not root.left and not root.right: 
            ret[0] += 1
        helper(root.left, table, num_odds)
        helper(root.right, table, num_odds)
        table[root.val] -= 1
        
    ret = [0]
    table = collections.Counter()
    helper(root, table, 0)
    return ret[0]