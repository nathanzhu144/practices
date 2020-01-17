# Nathan Zhu 6:13 pm, EHS 55 John Street August 4th, 2019
# Leetcode 449 | medium | medium
#
#       5
#    2    7
#  1  3  6  9
# 
# Note that with a preorder and inorder traversal, we can easily construct a unique tree.
# However, with a binary search tree, we can uniquely construct a tree with just a preorder.
# We can derive the inorder by sorting the preorder traversal.
#
#
# Here's a SUPER IMPORTANT thing when ending values to a string.  If you just convert the list
# to a string, you can't tell the difference between "34" and "3" "4". So, make sure the list
# is separated by spaces or something.
#

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


    def serialize(root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # store preorder
        # store inorder
        if not root: return []
        
        stack = [root]
        preorder = []
        while stack:
            curr = stack.pop()
            preorder.append(str(curr.val))
            if curr.right: stack.append(curr.right)
            if curr.left: stack.append(curr.left)
                
        return " ".join(preorder)
            
            
    def deserialize(data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data: return None
        
        preorder = map(int, data.split())
        inorder = sorted(preorder[:])

        # 1 2 3 inorder
        # 2 1 3 preorder
        # 1 3
        # See leetcode 105
        def preorder_inorder_tree(preorder, inorder):
            if not inorder: return None

            root = TreeNode(preorder.pop(0))
            root_index = inorder.index(root.val)
            root.left = preorder_inorder_tree(preorder, inorder[:root_index])
            root.right = preorder_inorder_tree(preorder, inorder[root_index + 1:])
            return root

        return preorder_inorder_tree(preorder, inorder)



## This is just testing functions ##

# Helper function.
def make_tree(vector):
    if not vector: return None
    if len(vector) == 1: return TreeNode(vector[0])
    mid = len(vector) // 2
    
    root = TreeNode(vector[mid])
    root.left = make_tree(vector[:mid])
    root.right = make_tree(vector[mid + 1:])
    return root


if __name__ == "__main__":
    tree = serialize(make_tree([1, 2, 3]))
    treestring = deserialize(tree)
    temp = treestring