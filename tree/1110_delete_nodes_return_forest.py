# Nathan Zhu, Monda July 8th, 2019, 3:02 pm.  
# Leetcode 1110 | medium | not too bad, medium?
#
# Given the root of a binary tree, each node in the tree has a distinct value.
# After deleting all nodes with a value in to_delete, we are left with a forest
#  (a disjoint union of trees).
# Return the roots of the trees in the remaining forest.  You may return the result 
# in any order
#
# This problem is pretty straightforward.  When I solved the problem, I did it without passing 
# state from parent to child, but there's a "slightly" more straightward answer where you pass state
# from parent to child.  The state is whether that node has a parent.  If it does NOT have a parent
# append it to ret.
# 
# Both solutions are here.
def del_nodes_no_state_pass(root, to_delete):
    """
    :type root: TreeNode
    :type to_delete: List[int]
    :rtype: List[TreeNode]
    """
    def helper(root, to_delete, ret):
        if not root: return None
        # If root.val is none, we need to do several things.
        # 1. If root has a left or a right:
        #    - if root_left not in to_delete, we append it as a new root
        #    - call helper on root.left
        #    - do same for root_right
        # 2. Return None, to prune original parent tree.
        if root.val in to_delete:
            if root.left:
                if root.left.val not in to_delete: ret.append(root.left)
                helper(root.left, to_delete, ret)
            if root.right: 
                if root.right.val not in to_delete: ret.append(root.right)
                helper(root.right, to_delete, ret)
            return None
        else:
            root.left = helper(root.left, to_delete, ret)
            root.right = helper(root.right, to_delete, ret)
            return root
    
    ret = list()
    # we append a parent iff not in to_delete
    if root.val not in to_delete: ret.append(root)
    helper(root, to_delete, ret)
    return ret



def del_nodes_state_pass(root, to_delete):
    def helper(root, to_delete, has_parent):
        if not root: return None
        if root.val in to_delete:
            helper(root.left, to_delete, has_parent = False)
            helper(root.right, to_delete, has_parent = False)
            return None
        else:
            if not has_parent:
                ret.append(root)
            root.left = helper(root.left, to_delete, has_parent = True)
            root.right = helper(root.right, to_delete, has_parent = True)
            return root
    
    ret = list()
    helper(root, to_delete, False)
    return ret