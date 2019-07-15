#  Nathan Zhu Amex Tower, Sunday 8:16 pm 
#  Leetcode 106, medium difficulty
#  Similar to preorder inorder in idea (leetcode 105)
#  Given a inorder and postorder traversal, how to recursively construct a BST
#   
# inorder = [9,3,15,20,7]
# postorder = [9,15,7,20,3]
# Return the following binary tree:
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 
#          3               [9] [15, 20, 7]
#            \ 
#            20
# One powerful obervation for this problem is that the last element of postorder
# is the root of the whole tree.
#
# Second to last in postorder is right child of root
#
# Third to last in postorder is right child of right child of root...
#
# 
# Construction:
# We take end off of postorder, and use that index to split inorder traversal
# Then, we build right side of subtree first, as that is the "right" direction
# to build in bc of how postorder traversal works.

def inorder_postorder(inorder, postorder):

    """
    :type inorder: List[int]
    :type postorder: List[int]
    :rtype: TreeNode
    """
    def helper(inorder, postorder):
        # there is no case where postorder is empty, but inorder
        # is not empty, every time we divide inorder by 2, but we
        # subtract postorder size by 1
        if not inorder: return None

        # We take back of the postorder, this is root
        root = TreeNode(postorder.pop(-1))

        # we first build right side of subtree
        # then we build left side of subtree
        root.right = helper(inorder[inorder.index(root.val) + 1 : ], postorder)
        root.left = helper(inorder[ : inorder.index(root.val)], postorder)

        return root

    return helper(inorder, postorder)

    