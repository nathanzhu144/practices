#  Nathan Zhu, Wednesday 10:30 pm, 55 John Street, New York, NY our AC broke and it is so hot
#  Leetcode 865 | medium | I think damn cool
#
#  I have been thinking about this for a few days.
#
#  Understanding this question wasn't quite easy, but we want to find the LCA of all th deepest branches in a BT
#  So, we first do a O(N) traversal of tree, and make a hash table calculating height of each node
#
#  Then, using that info, let's think of a base case.
#
#  Given just a node, we know that LCA of deepest nodes is DEEPER of left or right.
#  If left or right have same height, then we know that it is the LCA of the deepest nodes in tree.  That's it.
#
#  I love this problem


# A slightly better and more consise version (Jan 20th, 2020 10:10 pm ET, Ann Arbor MI, Foundry Lofts)
def subtreeWithAllDeepest(self, root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    table = dict()
    
    def find_h(root):
        if not root: return 0
        if root in table: return table[root]
        table[root] = 1 + max(find_h(root.left), find_h(root.right))
        return table[root]
        
    def helper(root):
        left, right = find_h(root.left), find_h(root.right)
        
        if left == right: return root
        if left > right: return helper(root.left)
        else: return helper(root.right)
        
    return helper(root)

# Wrote this at John Street.
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


