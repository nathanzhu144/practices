/*  Nathan Zhu April 14th, 2020 I think this postorder traversal way is much cooler than the level order traversal way.
*   Leetcode 199 | medium | not bad
*   Category: binary tree
*/

#include <unordered_map>
#include <vector>

struct TreeNode {
      int val;
      TreeNode *left;
      TreeNode *right;
      TreeNode() : val(0), left(nullptr), right(nullptr) {}
      TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
      TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

using namespace std;

int helper(TreeNode* root, int depth, unordered_map<int, int>& table){
    if(!root) return 0;
    if(!table.count(depth)) table[depth] = root->val;
    return 1 + max(helper(root->right, depth + 1, table), helper(root->left, depth + 1, table));
}

vector<int> rightSideView(TreeNode* root) {
    unordered_map<int, int> table;
    vector<int> ret;
    
    int max_depth = helper(root, 0, table);
    for(int i = 0; i < max_depth; ++i){
        ret.push_back(table[i]);
    }
    
    return ret;
}