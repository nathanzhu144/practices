/*  Nathan Zhu April 17th, 2020 Starting at salesforce tomorrow!!
 *  Leetcode 1379 | medium | easy
 *  Category: Binary tree
 *  This question kinda boring.
*/


struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

TreeNode* helper(TreeNode* original, TreeNode* cloned, TreeNode* target){
    if(!original) return nullptr;
    
    if(target == original) return cloned;
    
    auto left = helper(original->left, cloned->left, target);
    auto right = helper(original->right, cloned->right, target);
    
    return (left == nullptr) ? right : left;
}

TreeNode* getTargetCopy(TreeNode* original, TreeNode* cloned, TreeNode* target) {
    return helper(original, cloned, target);
}