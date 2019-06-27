#   Nathan Zhu, 9:40 pm, New York, 55th John Street
#   Leetcode 865 | medium | I think awesome
#   This is a damn cool problem - it makes perfect sense now, but it is such a good question.
#
#   So, the idea is that for all the deepest branches of a tree, we must have a LCA.  Return the LCA
#   of all of the deepest nodes.
#
#   While height of a subtree is not balanced, we go to the deeper side, as the LCA of the deepest branches must be
#   on that side.  If we ever get to a point where left and right subtrees have same height (we use a hash table with 
#   nodes to tree heights or both are nullpointers), we just return that node


def subtreeWithAllDeepest(root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    # goes thru tree, saves height of each node in a hash table
    def find_height(root, node_to_height):
        if not root: return 0
        node_to_height[root] = max(find_height(root.left, node_to_height), find_height(root.right, node_to_height)) + 1
        return node_to_height[root]
    
    def return_subtree_deepest_nodes(root, node_to_height):
        # root.left is None, but root.right is not None, right is deeper -> deepest subtree is on right
        if not root.left and root.right: return return_subtree_deepest_nodes(root.right, node_to_height)
        # root.right is None, but root.left is not None, left is deeper -> deepest subtree is on left
        if not root.right and root.left: return return_subtree_deepest_nodes(root.left, node_to_height)
        # left and right have equal height - this is LCA of all deepest branches, return this
        if not root.right and not root.left or node_to_height[root.left] == node_to_height[root.right]: return root
        # we know both root.left and root.right exist at this point, and are unequal
        # so, return the deeper of the two
        return return_subtree_deepest_nodes(root.left, node_to_height) \
            if node_to_height[root.left] > node_to_height[root.right] else return_subtree_deepest_nodes(root.right, node_to_height)
        
    node_to_height = dict()
    find_height(root, node_to_height)
    return return_subtree_deepest_nodes(root, node_to_height)