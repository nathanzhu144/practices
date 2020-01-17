    #  Nathan Zhu, Sunday 1:12 am Chicago.  Trying them trees.
    #  The idea behind LCA is simple.
    #
    #  I think the big idea is to think about what you need to know
    #  at each node rather than get overwhelmed by the whole problem
    #
    #  For example, if a node cannot find p and q in its right subtree
    #  it cannot be a lowest common ancestor, so we look into left subtree
    #
    #  Also, if p and q are found in the left and right subtrees, it
    #  is certainly true this node is LCA.
    
    
    def lca(root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def helper(root, p, q):
            if not root: return None
            
            # If looking for p or q, return myself.
            if p == root or q == root: return root

            # did not find me, so look in the left and right subtrees
            left = helper(root.left, p, q)
            right = helper(root.right, p, q)

            # This is LCA, return it
            if left and right: return root
            # We search the left and right subtrees
            if left: return left
            if right: return right
        return helper(root, p, q)