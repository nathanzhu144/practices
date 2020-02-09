# Nathan Zhu Jan 20th, 2020 10:30 pm 
# Leetcode 958 | medium | medium
# Category: Binary tree
# So, I did this question in C++ with a level order traversal,
# now, saw a heap-indexing soln.  This one is cooler.


# Intuition:
# Runtime: O(N)
# Space  : O(h)
# In a complete binary tree, the maximim right tree index (with 1 based indexing)
def isCompleteTree(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    # Returns a pair:
    # (num nodes in subtree, maximum right index)
    # In a complete binary tree, the maximim right tree index (with 1 based indexing)
    # should be equal to number of nodes in subtree.
    
    def helper(root, coord):
        if not root: return 0, 0   
        
        l = helper(root.left, 2 * coord)
        r = helper(root.right, 2 * coord + 1)
        
        tot_nodes = l[0] + r[0] + 1
        right_most = max(coord, l[1], r[1])
        return tot_nodes, right_most
    
    if not root: return True
    tot_nodes, right_most = helper(root, 1)
    return tot_nodes == right_most