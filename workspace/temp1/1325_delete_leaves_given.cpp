/** Nathan Zhu June 4th, 2020 A year + 2 days since I started leetcoding.  Man so much has changed!
 *  Leetcode 1325 | medium | medium
 *  Category: Tree, postorder traversal.
 */ 
 struct TreeNode {
      int val;
      TreeNode *left;
      TreeNode *right;
      TreeNode() : val(0), left(nullptr), right(nullptr) {}
      TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
      TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 };
 
class Solution {
public:
    TreeNode* helper(TreeNode* root, int target){
        if(!root) return nullptr;
        auto left(helper(root->left, target)), right(helper(root->right, target));
        if(!left && !right && root->val == target){
            //delete root; root = nullptr; Why is there a heap use after free when I delete here?
            return nullptr;
        }
        root->left = left;
        root->right = right;
        return root;
    }
    
    TreeNode* removeLeafNodes(TreeNode* root, int target) {
        return helper(root, target);
    }
};