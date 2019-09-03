# Nathan Zhu, Wednesday August 21st, 2019, 5:58 pm.  Stockton California, Second floor of house.
# Leetcode 1120 | medium | EZ yo
# Category: Tree
#
# Question: Find the subtree with the largest average value.

def maximumAverageSubtree(Sroot):
    """
    :type root: TreeNode
    :rtype: float
    """
    ret = [float("-inf")]
    
    # Pair for helper function is of [double (total value), int (num nodes)]
    def helper(root):
        if not root: return [0, 0]
        
        left = helper(root.left)
        right = helper(root.right)
        
        # The float conversion is needed here, otherwise integer division is done in python
        ret[0] = max(ret[0], (root.val + left[0] + right[0]) / float(1  + left[1] + right[1]))
        return [root.val + left[0] + right[0], 1  + left[1] + right[1]]
    
    helper(root)
    return ret[0]


# // This is the working C++ code.  Passed on first try yo.
# double average = -1;

# // Should return 
# pair<double, int> helper(TreeNode* root){
#     if(!root) return {0, 0};
    
#     pair<double, int> left = helper(root->left);
#     pair<double, int> right = helper(root->right);
#     double curr_avg = (root->val + left.first + right.first) / (1 + left.second + right.second);
    
#     average = max(curr_avg, average);
#     return {root->val + left.first + right.first, 1 + left.second + right.second};
# }


# double maximumAverageSubtree(TreeNode* root) {
#     helper(root);
#     return average;
# }