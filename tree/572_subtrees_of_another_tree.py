# Nathan Zhu Subtree of another tree
# Leetcode 572 | easy | yeah easy
#
# Returns true if s is a subtree of t.

def is_subtree(s, t):
    """
    :type s: TreeNode
    :type t: TreeNode
    :rtype: bool
    """
    def same_tree(t1, t2):
        if not t1 or not t2: return not t1 and not t2
        return t1.val == t2.val and same_tree(t1.left, t2.left) and same_tree(t1.right, t2.right)
    
    def helper(s, t):
        if not s or not t: return not s and not t
        else:
            return same_tree(s, t) or helper(s.left, t) or helper(s.right, t)
    return helper(s, t)