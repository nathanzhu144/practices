# Nathan Zhu May 13th, 2020. Stockton, CA. 3:04 am, time never sleeps huh.
# Leetcode 1302 | medium | damn good question
# Category: binary tree
# Similar idea to root with deepest nodes in terms of thinking

import collections

def deepestLeavesSum(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    
    h_table = collections.Counter()
    
    def get_h(node):
        if not node: return 0
        if node in h_table: return h_table[node]
        left, right = get_h(node.left), get_h(node.right)
        h_table[node] = max(left, right) + 1
        return h_table[node]
    
    def helper(root):
        if not root: return 0
        if not root.left and not root.right: return root.val
        if get_h(root.left) > get_h(root.right): return helper(root.left)
        if get_h(root.right) > get_h(root.left): return helper(root.right)
        return helper(root.left) + helper(root.right)
    
    get_h(root)
    return helper(root)