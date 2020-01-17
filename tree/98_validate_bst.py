# Nathan Zhu Jan 9th, 2019 During SI-106 lecture.  
# Leetcode 98 | medium | med
# Category: Binary tree
#
# Two O(N) ways to do this problem where N is num of nodes in tree.
# 1. Do inorder traversal, and verify everything is in proper place (can be done in O(1) space, but not by a human?)
# 2. Pass the conditions recursively (elegant)  O(1) space except stack


def isValidBST(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    
    
    def valid(root, left, right):
        if not root: return True
        
        if not left < root.val < right: return False
        
        return valid(root.left, left, min(root.val, right)) and valid(root.right, max(root.val, left), right)
    
    return valid(root, float("-inf"), float('inf'))