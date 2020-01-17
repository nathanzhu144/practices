#  Nathan Zhu American Express Building, Sunday 6:17 pm, June 23rd, 2019
#  How to construct a binary tree from preorder and inorder traversal?
#  This is leetcode 105, it is a medium question.
#
#  preorder = [3,9,20,15,7]
#  inorder = [9,3,15,20,7]
# 
#      3
#    / \
#   9  20
#     /  \
#    15   7
#
#  Note, we first split inorder at...
#   inorder = [9,3,15,20,7]
#                ^ split
#            /         \
#          [9]       [15, 20, 7]
#          /             \
#                      [15] [7]
#
def buildTree(preorder, inorder):
    """
    :type preorder: List[int]
    :type inorder: List[int]
    :rtype: TreeNode
    """
    def helper(preorder, inorder):
        # If preorder is empty, inorder must be empty
        # If inorder is empty, preorder prob is not empty
        # We split inorder in half every time, by only decrease preorder by 1
        if not inorder: return None
        
        # Preorder gives us value of the root node
        root = TreeNode(preorder.pop(0))
        
        # we recursively build rest of the tree.
        # note where we split the inorder array
        # we take the front element of the preorder (the root), and 
        # split it according to the index of that element in preorder (see picture)
        # NOTE: YOU HAVE TO BUILD LEFT BEFORE RIGHT
        root.left = helper(preorder, inorder[:inorder.index(root.val)])
        root.right = helper(preorder, inorder[inorder.index(root.val) + 1:])
        
        return root
    return helper(preorder, inorder)