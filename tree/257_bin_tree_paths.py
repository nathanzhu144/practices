# Nathan Zhu January 3rd, 2019 9:57 pm
# Leetcode 257 | easy | EZ
# Category: binary tree

# Basic tree problem with some backtracking

def binaryTreePaths(root):
    """
    :type root: TreeNode
    :rtype: List[str]
    """
    
    
    ret = []
    
    def convert_to_print(arr):
        ret = []
        for i, num in enumerate(arr):
            ret.append(str(num))
            if i != len(arr) - 1: ret.append("->")
        return "".join(ret)
    
    def helper(root, path):
        if not root: return
        
        path += [root.val]
        
        if not root.left and not root.right:
            ret.append(convert_to_print(path))
        
        helper(root.left, path)
        helper(root.right, path)
        path.pop()
        
    helper(root, [])
    return ret
        