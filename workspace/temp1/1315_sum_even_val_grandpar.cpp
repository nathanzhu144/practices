/** May 4th, 2020 Stockton, CA.  No meeting thursday today at SF!
 *  Leetcode 1315 | medium | medium
 *  Category: Tree
 */

struct TreeNode{
    TreeNode* left;
    TreeNode* right;
    int val;
};
int helper(TreeNode* root, TreeNode* p, TreeNode* gp){
    if(!root) return 0;
    auto ret = helper(root->left, root, p) + helper(root->right, root, p);
    return (gp && gp->val % 2 == 0) ? root->val + ret : ret;
}
int sumEvenGrandparent(TreeNode* root) {
    return helper(root, nullptr, nullptr);
}