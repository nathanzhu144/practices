#  Nathan Zhu Friday 10:49 am, Amex building, July 12th, 2019
#  Leetcode 894 | medium | sure, medium
#  Category:  Tree/Recursion
#  
#  Nodes: 0  0  0  0  0 
#  Index: 1  2  3  4  5
#
#  So, we arbitrary select an index, and recur.  See leetcode 95, unique binary trees II.  The only difference here is 
#  1 insight.  To make a full binary tree, each node has to be even or odd.  It is only possible to make a fully tree
#  with an odd number of nodes.  
#
#  Also, a full binary tree is by definition composed of full binary trees.  So, to recursively make all full binary trees,
#  we must only use the "even" indices as roots, whereas to make ALL possible trees, we use every index as a root.   
#  NOTE: index is 1-indexed.

def all_poss_fully_bin_trees(n):
    def helper(index):
        # We use 1-based indexing for the tree nodes
        # if index <= 0: return [None]   # not necessary
        if index == 1: return [TreeNode(0)]

        returned_trees = []
        counter = 2       # we use only even nodes as roots.

        while counter < index:
            for left in helper(counter - 1):
                for right in helper(index - counter):
                    root = TreeNode(0)
                    root.left = left
                    root.right = right
                    returned_trees.append(root)
            counter += 2

        return returned_trees
    return helper(N)