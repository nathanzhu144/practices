/* Nathan Zhu Sunday Stockton, CA. 11:59 pm June 19th, 2020.  I watched a william lin video of him doing 150 questions in 12 hours lol.  OK my dude.
*  Leetcode 971 | medium | medium
*  Category: BST, greedy
*  
*  Flip if we have to.  The problem is misleading in that it indicates some methods of flipping nodes will lead to more moves
*  It is really more obvious.  We attempt to do a preorder traversal, and if the value doesn't match, we try flipping.
*  If that still doesn't work (we see in next recursive call), we return false.
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

class TreeNode{
private:
public:
    TreeNode* left;
    TreeNode* right;
    int val;
};


vector<int> ret;

bool helper(TreeNode* root, vector<int>& voyage, int& i){
    if(!root) return true;
    // A previous flip still led to a unworkable sequence.
    if(root->val != voyage[i++]) return false;                
    auto l(root->left), r(root->right);
    
    // If left's value != next val in journey, we obviously need to swap.  
    if(root->left && root->left->val != voyage[i]){
        swap(l, r);  // swaps our pointer copies, not pointers on BST.
        ret.push_back(root->val);
    }
        
    return helper(l, voyage, i) && helper(r, voyage, i);
}

vector<int> flipMatchVoyage(TreeNode* root, vector<int>& voyage) {
    int i = 0;
    return helper(root, voyage, i) ? ret : vector<int>(1, -1);  
}