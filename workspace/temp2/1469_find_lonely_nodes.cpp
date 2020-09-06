
/* Nathan Zhu Tuesday July 14th, 2020  Stockton, CA. TACO TUESDAY
*  Deploying golang projects to Heroku is really fun.  :P
*  Leetcode 729 | medium | medi
*  Category: Design
*/


#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <set>
#include <stack>
#include <string>
#include <queue>
#include <deque>
#include <utility>
#include <algorithm>
#include <cmath>
#include <limits>
#include <iostream>

using namespace std;



struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
};

void helper(TreeNode* root, vector<int>& ret){
    if(!root) return;
    if(!root->left && root->right) ret.push_back(root->right->val);
    if(!root->right && root->left) ret.push_back(root->left->val);
    helper(root->left, ret);
    helper(root->right, ret);
}

vector<int> getLonelyNodes(TreeNode* root) {
    vector<int> ret;
    helper(root, ret);
    return ret;
}