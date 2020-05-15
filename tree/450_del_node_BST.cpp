/** Nathan Zhu May 4th, 2020.  Stockton, CA, COVID-19.  Crushed that Binary search question on the 376 final, Meera's birthday yesterday
 *  Leetcode 450 | medium | kinda hard tbh, in how to get an inorder node to delete
 *  Category: Binary tree
 * */
 struct TreeNode {
     int val;
     TreeNode *left;
     TreeNode *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
  };
 
class Solution {
public:
    TreeNode* inorder(TreeNode* root){
        root = root->right;
        while(root->left) root = root->left;
        return root;
    }
    TreeNode* deleteNode(TreeNode* root, int key) {
        if(!root) return root;  // key not found
        else if(root->val < key) root->right = deleteNode(root->right, key);
        else if(root->val > key) root->left = deleteNode(root->left, key);
        else if(root->val == key){
            if(!root->left) return root->right;      // deleted leaf node or node with only a right node.
            else if(!root->right) return root->left; // deleted leaf node or node with only a left node.
            else{
                int inor = inorder(root)->val;
                root->val = inor;
                root->right = deleteNode(root->right, inor);
            }
        }
        return root;
    }
};