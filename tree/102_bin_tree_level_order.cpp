/* Nathan Zhu Jan 10th, 2020 7:27 pm Foundry Lofts
*  Leetcode 102 | medium | EZ
*  Category: binary tree
*/
 
 struct TreeNode {
     int val;
      TreeNode *left;
      TreeNode *right;
      TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 };
 
#include <vector>

using namespace std;
vector<vector<int>> levelOrder(TreeNode* root) {
    vector<vector<int>> ret;
    if(!root) return ret;
    
    vector<TreeNode*> q = {root};
    
    while(!q.empty()){
        vector<TreeNode*> new_q;
        vector<int> level;
        for(auto& tn: q) {
            level.push_back(tn->val);
            if(tn->left) new_q.push_back(tn->left);
            if(tn->right) new_q.push_back(tn->right);
        }
        q = new_q;
        ret.push_back(level);
    }
    
    return ret;
}