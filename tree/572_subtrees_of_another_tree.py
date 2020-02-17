# Nathan Zhu ?? Date Subtree of another tree
# Nathan Zhu Feb 9th, 2020.  The idea of using a fenkle hash is pretty non-obvious.
# Leetcode 572 | easy | yeah easy
#
# Returns true if s is a subtree of t.
from hashlib import sha256

# O(S) * O(T) soln
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

# O(S) + O(T) soln
def isSubtree(self, s, t):
    """
    :type s: TreeNode
    :type t: TreeNode
    :rtype: bool
    """
    
    table = dict()
    
    def hash_(x):
        S = sha256()
        S.update(x)
        return S.hexdigest()
    
    def find_merkle(node):
        if not node: return "#"
        lefth = find_merkle(node.left)
        righth = find_merkle(node.right)
        table[node] = hash_(lefth + hash_(str(node.val)) + righth)
        return table[node]
    
    def helper(curr, target):
        if not curr: return False
        
        return table[curr] == table[target] or helper(curr.left, target) or helper(curr.right, target)
    
    find_merkle(s)
    find_merkle(t)
    return helper(s, t)