# Nathan Zhu Saturday 11:54 am Starbucks State Street
# Leetcode 545 | medium | kinda hard
# 
# I really don't like this question because it is very ambiguous what
# a left boundary/right boundary is.


def boundaryOfBinaryTree(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    # 2 cases when we continue a left boundary / right boundary
    # We talk about left, but right is the same
    # 1. it is already on left boundary (for left recursive call)
    # 2. root.left is null, and isleft (for right recursive call)
    #
    # Other question is: how do we make sure we don't repeat add elements
    # A node cannot be both left and right except root, so we don't worry about
    # that.
    #
    # We only need to worry about leaf conflicting w left or right, so
    # we only add to leaf if not left and not right
    #
    # 
    # Finally, we worry about how to make a counterclockwise orientation.
    # This is easy, we add left and leaf elements on pre-order side of things,
    # and add right on postorder side of things.
    ret = []
    def helper(root, left, right):
        if not root: return
        isleaf = not root.left and not root.right
        
        if left: ret.append(root.val)
        if not left and not right and isleaf: ret.append(root.val)
            
        helper(root.left, left, right and root.right == None)
        helper(root.right, left and root.left == None, right)
        
        if not left and right: ret.append(root.val)
    
    # The only node on left & right boundary is root, so we handle
    # it shlightly differently
    if root:
        ret.append(root.val)
        helper(root.left, True, False)
        helper(root.right, False, True)
        
    return ret