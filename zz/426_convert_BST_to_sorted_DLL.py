
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
    def merge(node1, node2):
        # Step 1: Init newtail1 and newtail 2 at heads respectively
        # node1  H1A -> 1B -> 1C -> H1A
        #         ^newtail1
        #
        # node2  H2A -> 2B -> 2C -> H2A
        #         ^newtail2
        # Step 2: Make new tail 
        # node1  H1A -> 1B -> 1C -> H1A
        #                      ^newtail1
        #
        # node2  H2A -> 2B -> 2C -> H2A
        #                      ^newtail2
        # Step 3: Turn both into singly linked list
        # node1  H1A -> 1B -> 1C -> None
        #                      ^newtail1
        #
        # node2  H2A -> 2B -> 2C -> None
        #                      ^newtail2
        # Step 4: Link both, nodetail1.right = node2
        #                    nodetail2.right = node1
        #                    node2.left = nodetail1
        #                    node1.left = nodetail2
        #           
        #                      v newtail1
        # node1  H1A -> 1B -> 1C
        #         ^    --------
        #         ^----v------- 
        #         v----v      ^
        # node2  H2A -> 2B -> 2C
        #                      ^newtail2
        if not node1: return node2
        if not node2: return node1
        
        # Step 1
        newtail1, newtail2 = node1, node2
        # Step 2
        while newtail1.right != node1:
            newtail1 = newtail1.right
        while newtail2.right != node2:
            newtail2 = newtail2.right
        
        # Step 3
        # connect tail with heads
        # connect head with tails
        newtail1.right = node2
        newtail2.right = node1
        node2.left = newtail1
        node1.left = newtail2
        return node1
        
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
            