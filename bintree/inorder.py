# Nathan Zhu June 18th, 2019 
# 55 John Street, New York NY, 8:35 pm
# just a primer on inorder traversal, note that inorder gives you an in-order
#                                               sequence for a binary tree

# Recursive is trivial
def inorder_rec(root, returned):
    if not root: return
    inorder_rec(root.left, returned)
    returned.append(root.val)
    inorder_rec(root.right, returned)

# Iterative is more nuanced
def inorder(root):
    if not root: return []
    returned, tree_stack = list(), list()
    curr = root

    #  NOTE:
    # Why curr or tree_stack?
    # See this example.
    #  Ex. 5
    #       \
    #        6
    #  
    #  NOTE: nullptrs never enter tree stack
    while curr or tree_stack:
        while curr:
            tree_stack.insert(0, curr)
            curr = curr.left

        #           5
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
        # top of tree_stack contains element we want to print
        # in our inorder traversal as we have gone as far left as possible
        curr = tree.pop(0)
        returned.append(curr.val)

        #           5
        #         /
        #        3
        #       / 
        #      2 
        #       \
        #        2.7  <- we add right, now, then on next while loop go to 2.5
        #      /
        #     2.5
        # we now are doing the call on right subtree.  On the right tree,
        # when we get to the right child, we must again go as far left as possible
        # while curr or tree will take care of this
        #
        #           5
        #         /
        #        3
        #       / 
        #      2    2 has no right, next while loop pops 2 off, and we go see if 3 has a right
        # if curr.right is None, we will pop the next thing off the stack,
        curr = curr.right
    return returned
    