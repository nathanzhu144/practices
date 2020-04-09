# Nathan Zhu April 7th, 2020. 12:01 am.  Foundry Lofts, COVID-19
# Leetcode 297 | hard | not bad
# Category; binary tree

# This is a different way than I usually do it with pre-order and in-order traversal.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def helper(root):
            if not root: return "X,"
            left = helper(root.left)
            right = helper(root.right)
            return str(root.val) + "," + left + right
        return helper(root)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        
        :type data: str
        :rtype: TreeNode
        """
        def helper(arr):
            currval = arr.pop()
            
            if currval == "X": return None
            
            curr = TreeNode(int(currval))
            curr.left = helper(arr)
            curr.right = helper(arr)
            return curr
            
        arr = data.split(",")[::-1]
        return helper(arr)