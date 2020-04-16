# Nathan Zhu SI 106 exam tomorrow woooo
# Leetcode 222 | medium | damn cool
# Category: Tree, divide conq
# Log(LogN) runtime


def countNodes(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    def find_height(root):
        ret = 0
        while root:
            ret += 1
            root = root.left
        return ret
    
    
    def helper(root):
        if not root: return 0
        
        lefth = find_height(root.left)
        righth = find_height(root.right)
        
        if lefth > righth: return helper(root.left) + 2 ** righth
        else: return helper(root.right) + 2 ** lefth
        
    return helper(root)