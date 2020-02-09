# Nathan zhu Saturday January 18th, 2020 11:45 am Starbucks State Street 
# Leetcode 199 | medium | not bad
# Category: tree
#
# So, I usually do the queue soln where you do a standard level order traversal
# but you save the rightmost node in each traversal.  This soln is cooler, if same efficiency
# Note how we recurse to right before left, ensuring we reach rightmost nodes first.
# Everytime we hit a new level, we add it to list.

def rightSideView(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    ret = []
    def helper(root, level):
        if not root: return
        if level >= len(ret): ret.append(root.val)
        helper(root.right, level + 1)
        helper(root.left, level + 1)
    helper(root, 0)
    return ret