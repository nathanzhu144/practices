# Nathan Zhu, June 14th, 2020
# Leetcode 297 | hard | kinda hard
# Category: Binary tree
# LOL DESERIALIZE IS HILARIOUS.

import collections
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, l, r):
        self.val = x
        self.left = l
        self.right = r

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def helper(root):
            if not root: return ["#"]
            ret = [str(root.val)]
            ret += helper(root.left)
            ret += helper(root.right)
            return ret
        
        return " ".join(helper(root))
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        q = collections.deque(data.split())
        def helper():
            curr = q.popleft()
            return None if curr == "#" else TreeNode(int(curr), helper(), helper())   #I like this line

        return helper()

        # More readable version
        # q = collections.deque(data.split())
        # def helper():
        #     curr = q.popleft()
        #     if curr == "#": return None
        #     ret = TreeNode(int(curr), helper(), helper())
        #     return ret
        
        
        # return helper()
        