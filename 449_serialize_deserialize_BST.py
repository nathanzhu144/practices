

#       5
#    2    7
#  1  3  6  9
# 
# Note that with a preorder and inorder traversal, we can easily construct a unique tree.
# 
#
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
    # assume root is not null, standard iterative preorder traversal.
    def pre_order(root):
        stack = [root]
        preorder = list()
        while stack:
            curr = stack.pop()
            preorder.append(str(curr.val))
            if curr.right: stack.append(curr.right)
            if curr.left: stack.append(curr.left)
        
        return preorder

    if not root: return ""
    preorder_list = pre_order(root)
    # operations are right to left, so I sort a copy of preorder_list instead of actual list
    return "".join(preorder_list) + "|" + "".join(sorted(preorder_list[:]))

    

def deserialize(data):
    """Decodes your encoded data to tree.
    
    :type data: str
    :rtype: TreeNode
    """
    preorder, inorder = data.split("|")
    preorder, inorder = [int(c) for c in preorder], [int(c) for c in inorder]

    # 1 2 3 inorder
    # 2 1 3 preorder
    # 1 3
    # See leetcode 105
    def preorder_inorder_tree(preorder, inorder):
        if not inorder: return None
        
        root_index = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[root_index])
        root.left = preorder_inorder_tree(preorder, inorder[:root_index])
        root.right = preorder_inorder_tree(preorder, inorder[root_index + 1:])
        return root

    return preorder_inorder_tree(preorder, inorder)


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