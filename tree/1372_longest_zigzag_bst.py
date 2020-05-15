# Nathan Zhu May 7th, 2020. Saw Amber today while walking with Renying, they are abouta have finals.
# Leetcode 1372 | medium | not too bad
# Category: tree
# My runtime on this one is N^2, but we should be able to get O(N)

def longestZigZag(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    ret = [0]
    
    def helper(root, lastdir, n):
        ret[0] = max(ret[0], n)
        if not root: return
        
        if lastdir == "left":
            helper(root.right, "right", n + 1)
            helper(root.left, "left", 0)
        else:
            helper(root.left, "left", n + 1)
            helper(root.right, "right", 0)
            
        
    helper(root.left, "left", 0)
    helper(root.right, "right", 0)
    return ret[0]