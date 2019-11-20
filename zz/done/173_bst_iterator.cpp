// Nathan Zhu
// Leetcode 173 | medium | med
// Category: BST

#include <stack>

using namespace std;


struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 };



class BSTIterator {
private:
    stack<TreeNode*> s;
public:
    BSTIterator(TreeNode* root) {
        find_left(root);
    }
    
    /** @return the next smallest number */
    int next() {
        TreeNode* curr = s.top();
        s.pop();
        
        if(curr->right){
            find_left(curr->right);
        }
        return curr->val;
    }
    
    /** @return whether we have a next smallest number */
    bool hasNext() {
        return !s.empty();
    }
    
    void find_left(TreeNode* root){
        TreeNode* curr = root;
        while(curr){
            s.push(curr);
            curr = curr->left;
        }
    }
};