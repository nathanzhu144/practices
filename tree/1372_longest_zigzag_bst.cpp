/* Nathan Zhu Friday April 9th, 2020.  Think I am getting better at C++ now, 
*  Leetcode 1372 | medium | medium
*  Category: Binary tree
*
*  This is O(N) instead of the N^2 soln I did before
*/

#include <tuple>

using namespace std;
class TreeNode{
    public:
    TreeNode* left;
    TreeNode* right;
};

tuple<int, int, int> helper(TreeNode* root){
    if(!root) return {0, 0, 0};
    
    auto [ll, lr, totl] = helper(root->left);
    auto [rl, rr, totr] = helper(root->right);
    int ret = max(max(lr + 1, rl + 1), max(totl, totr));
    
    return {lr + 1, rl + 1, ret};

}
int longestZigZag(TreeNode* root) {
    return get<2>(helper(root)) - 1;
}