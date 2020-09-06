/* Nathan Zhu Sunday Stockton, CA. 9:24 pm June 19th, 2020.  I watched a william lin video of him doing 150 questions in 12 hours lol.  OK my dude.
*  Leetcode 987 | medium | medium
*  Category: binary tree, hard part is figuring out how to break ties correctly.
*/


#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <set>
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
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

// maxc indicates maximum column found
// minc indicates minimum column found
void dfs(TreeNode* root, int row, int col, int& minc, int& maxc, unordered_map<int, vector<vector<int>>>& col_to_node){
    if(!root) return;
    minc = min(col, minc);
    maxc = max(col, maxc);
    col_to_node[col].push_back({row, root->val});
    dfs(root->left, row + 1, col - 1, minc, maxc, col_to_node);
    dfs(root->right, row + 1, col + 1, minc, maxc, col_to_node);
}

vector<vector<int>> verticalTraversal(TreeNode* root) {
    unordered_map<int, vector<vector<int>>> col_to_node; // col -> <row, val>
    vector<vector<int>> ret;
    int maxc(0), minc(0);
    
    dfs(root, 0, 0, minc, maxc, col_to_node);
    for(int i = minc; i <= maxc; ++i){
        sort(col_to_node[i].begin(), col_to_node[i].end());
        vector<int> curr;
        for(auto& vec : col_to_node[i]) curr.push_back(vec[1]);
        ret.push_back(curr);
    }
    
    return ret;
}
