
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


def treeToDoublyList(root):
    """
    :type root: Node
    :rtype: Node
    """
    # node 1 and node 2 are both circularly linked list
    # node1 is "smaller val" linked list, node2 is "bigger val" linked list
    def merge(a, b):
        if not a: return b
        if not b: return a
        
        btail = b.left
        atail = a.left
        
        btail.right = a
        a.left = btail
        
        atail.right = b
        b.left = atail
        return a
        
    def helper(root):
        if not root: return None
        
        # we have recursed to left and right subtrees
        left = helper(root.left)
        right = helper(root.right)
        
        # We turn root into a circularly doubly linked list
        root.left = root
        root.right = root
        temp = merge(left, root)
        return merge(temp, right)
    
    return helper(root)
            