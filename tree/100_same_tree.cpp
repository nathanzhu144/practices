/** Nathan Zhu March 16th, 2020.  Coronavirus quarantine just started.  
 *  Leetcode 100 | easy | easy
 *  Category: Tree
 * 
 */

class TreeNode{
public:
     TreeNode* left; 
     TreeNode* right;
     int val;
};

bool isSameTree(TreeNode* p, TreeNode* q) {
    if(!p or !q) return !p && !q;
    return isSameTree(p->left, q->left) and isSameTree(p->right, q->right) and p->val == q->val;
}