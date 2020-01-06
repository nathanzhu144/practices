# Nathan Zhu 11:14 pm Saturday January 3rd, 2019, Think I'm coming down with a cold...
# Leetcode 428 | hard | not too bad
# Category: binary tree
#
# This is easier in some ways than serializing a binary search tree.  When you serialize a binary search tree, you have to care
# whether a node is the left or right node of a parent, whereas in this nary tree, it really doesn't matter - it is just part of a vector.
# 
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Codec:
    def ser_helper(self, root, ret):
        if not root: return ""
        ret += [str(len(root.children))]
        ret += [str(root.val)]
        
        for child in root.children:
            self.ser_helper(child, ret)
            
        return ret
    
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        ret = self.ser_helper(root, [])
        return " ".join(ret)
        

    
    def dser_helper(self, data, it):
        child_size, rootval = int(next(it)), int(next(it))
        
        root = Node(rootval, [])
        for i in range(child_size):
            root.children.append(self.dser_helper(data, it))
            
        return root
                

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data: return None
        newdata = data.split(" ")
        it = iter(newdata)
        root = self.dser_helper(newdata, it)

        return root

if __name__ == "__main__":
    c = Codec()
    c.deserialize("3 1 2 3 0 5 0 6 0 2 0 4")