

def preorder_rec(root):
    if not root: return
    returned, tree_stack = list(), list()
    curr = root
   
   #  We need an or curr for this reason...
   #  6
   #    \
   #     7
   #  Walk thru this
    while tree_stack or curr:
        #          5
        #         /
        #        3
        #       / 
        #      2    <- we get to here
        #       \
        #        2.7
        #      /
        #     2.5
        # at this point, curr is guaranteed to be None
        # also at this point, top of tree_stack is not none,
        # Unlike inorder traversal, we are DONE with element at top of stack now
        # we don't need to append to returned, as our while loop appends as it goes
        while curr:
            tree_stack.insert(0, curr)
            returned.append(curr.val)     # diff between this and inorder
            curr = curr.left
        
        # we simply pop the element, and set curr to its right child
        curr = tree.pop(0)
        curr = curr.right

    return returned