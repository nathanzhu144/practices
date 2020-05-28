
/* Nathan Zhu May 18th, 2020.  First day at Salesforce!
*  Leetcode 1382 | medium | easier with thsi way, hard in O(1) space.
*  Category: BST
*
*  I do the inorder iteratively, then make an array.  I convert the array to a BST. 
*/

#include <vector>

using namespace std;


class TreeNode {
public:
    TreeNode(int n){ val = n; }
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode* parent;
};

vector<int> inorder(TreeNode* root){
    vector<TreeNode*> stk;
    TreeNode* curr = root;
    vector<int> ret;
    if(!root) return vector<int>();
    
    while(stk.size() || curr){
        while(curr){
            stk.push_back(curr);
            curr = curr->left;
        }
        
        curr = stk.back();
        stk.pop_back();
        ret.push_back(curr->val);
        
        curr = curr->right;
    }
    
    return ret;
}

TreeNode* build(vector<int>& ordered, int l, int r){
    if(l > r) return nullptr;
    int mid = (r - l) / 2 + l;
    TreeNode* root = new TreeNode(ordered[mid]);
    root->left = build(ordered, l, mid - 1);
    root->right = build(ordered, mid + 1, r);
    return root;
}

TreeNode* balanceBST(TreeNode* root) {
    if(!root) return nullptr;
    vector<int> ordered = inorder(root);
    return build(ordered, 0, ordered.size() - 1);
}