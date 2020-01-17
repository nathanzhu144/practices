#  Nathan Zhu Amex Building, New York, NY, 36th floor
#  Sunday 10:27 am June 23rd, 2019
#  
#   given a positive integer depth d, for each NOT null tree nodes N in 
#   depth d-1, create two tree nodes with value v as N's left subtree root 
#   and right subtree root. And N's original left subtree should be the left 
#   subtree of the new left subtree root, its original right subtree should
#    be the right subtree of the new right subtree root. If depth d is 1 that 
#    means there is no depth d-1 at all, then create a tree node with value v 
#   as the new root of the whole original tree, and the original tree is 
#   the new root's left subtree.
import collections

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def add_one_row(root, val, depth):
    if depth == 1:
        newroot = TreeNode(val)
        newroot.left = root
        return newroot

    BFS_curr = collections.deque([root])
    BFS_next = collections.deque(list())

    while BFS_curr:
        for curr in BFS_curr:
            if curr.left: BFS_next.append(curr.left)
            if curr.right: BFS_next.append(curr.right)

        # At this point we have the current level in BFS_curr
        # and next level in BFS_next
        if depth == 2:
            for node in BFS_curr:
                # new left point to parent left
                # new right point to parent right
                newnodeleft = TreeNode(val)
                newnodeleft.left = node.left
                newnoderight = TreeNode(val)
                newnoderight.right = node.right

                # parent point to new children
                node.left = newnodeleft
                node.right = newnoderight
            return root

        BFS_curr = BFS_next
        BFS_next.clear()
        depth -= 1

    return root
            # do stuff