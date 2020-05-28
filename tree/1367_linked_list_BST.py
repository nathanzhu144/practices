# Nathan Zhu May 21st, 2020 11:25 pm, Stockton, CA, Thursday.  4th day of work at SF!
# Leetcode 1367 | medium | easy
# Category: Binary Tree

def isSubPath(self, head, root):
    """
    :type head: ListNode
    :type root: TreeNode
    :rtype: bool
    """
    def helper(head, root):
        if not head: return True
        if not root: return False
        if head.val != root.val: return False
        return helper(head.next, root.left) or helper(head.next, root.right)
    
    def traverse(head, root):
        if not root: return False
        if helper(head, root): return True
        return traverse(head, root.left) or traverse(head, root.right)
    return traverse(head, root)