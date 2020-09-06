/* Nathan Zhu Sunday, July 13th, 2020  Stockton, CA.  Saw Amber today while walking.  
*  Bought a lot of nepenthes veitchii (M) recently from Redleaf.  Excited to see them.  Also saw a surprisingly reddish pitcher
*  on my Akazukin x Candy stripe veitchii, I bought from Native exotics recently.  Also bought another candy x candy today.
*  Good stuff.
*  Leetcode 106 | medium | medium
*  Category: tree
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
    TreeNode* left;
    TreeNode* right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode* left, TreeNode* right) : val(x), left(left), right(right) {}
};



// helper
TreeNode* helper(vector<int>& inorder, vector<int>& postorder, int instart, int inend, unordered_map<int, int>& table){
    if(instart > inend) return nullptr;
    
    int pos = table[postorder.back()];
    TreeNode* root = new TreeNode(inorder[pos]);
    postorder.pop_back();
    root->right = helper(inorder, postorder, pos + 1, inend, table);
    root->left = helper(inorder, postorder, instart, pos - 1, table);
    return root;
}

//actual function
TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
    unordered_map<int, int> table;
    for(int i = 0; i < inorder.size(); ++i){
        table[inorder[i]] = i;
    }
    
    return helper(inorder, postorder, 0, inorder.size() - 1, table); 
}