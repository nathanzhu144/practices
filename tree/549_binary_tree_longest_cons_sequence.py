# Nathan Zhu Saturday December 28th, 2019
# Leetcode 549 | medium | medium
# Category: Binary tree (postorder traversal)

# This is similar to the ideas behind a lot of the postorder questions in binary tree questions.
# This soln does not use a global variable.


def longestConsecutive(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    def helper(root):
        if not root: return 0, 0, 0
        
        # What do we care about at this particular node?
        # 1. What is the longest increasing sequence INCLUDNG this node
        # 2. What is the longest sequence overall.
        #
        # So, 1. is not so easy.
        # To calculate that, we just care about this kind of structure,
        #
        #      4  (curr)     4  (curr)
        #    /  \           / \
        #  3    5    or    5   3
        #  /    /             /
        # 2    6             2
        #  inc on right    inc on left
        #  dec on left     dec on right
        #
        # At the recursive call of node 4 in the diagram above, we care about the maximum increasing sequence,
        # maximum decreasing sequence on left and right.  We take the longest inc, dec from left, longest inc, dec from right
        # If the value of left or right is one away, we can add this value onto the sequence.
        inc, dec = 1, 1
        left_inc, left_dec, left_ret = helper(root.left)
        right_inc, right_dec, right_ret = helper(root.right)
        
        if root.left:
            if root.left.val == root.val + 1: inc = 1 + left_inc
            if root.left.val == root.val - 1: dec = 1 + left_dec

        if root.right:
            if root.right.val == root.val + 1: inc = max(inc, 1 + right_inc)
            if root.right.val == root.val - 1: dec = max(dec, 1 + right_dec)

        return inc, dec, max(inc + dec - 1, left_ret, right_ret)
    
    
    return helper(root)[2]