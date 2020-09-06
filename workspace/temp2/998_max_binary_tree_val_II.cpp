/* Nathan Zhu Sunday, July 13th, 2020  Stockton, CA.  Saw Amber today while walking.  
*  Bought a lot of nepenthes veitchii (M) recently from Redleaf.  Excited to see them.  Also saw a surprisingly reddish pitcher
*  on my Akazukin x Candy stripe veitchii, I bought from Native exotics recently.  Also bought another candy x candy today.
*  Good stuff.
*  Leetcode 998 | medium | medium
*  Category: tree
*/

// This question is really confusing.  The idea behind this question is we take the array from max binary tree I, when 
// we use this array to construct the "max binary tree".   We consider pushing back a new value onto the end of that array, 
// and given the constructed max binary tree, how to make that constructed tree reflect the pushed back element?  


/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */


//  Ex1
//  1 2  7 3 4

//       7
//     /   \
//    2    4
//   /     /
//  1      3
     
//  1 2  7 3 4 3.5 push back (3.5)
     

//       7
//     /   \
//    2    4
//   /    /  \ 
//  1     3  3.5 (new)
      
     
// Ex2
//  7 4 3 2

//       7
//        \
//         4
//          \
//           3
//            \
//             2
     
//   7 4 3 2 5 push back (5)

//       7
//        \
//          5 (new)
//         /
//         4
//          \
//           3
//            \
//             2
            
//  Ideas: Look for a value until we reach a nullptr, or we reach a value s.t.
//         inserted value is greater than the current node's value.
     
//         If this condition of nullptr or inserted val > curr node value, which
//         side do we look?  Well, we look to the right.  Remember, since
//         we are recusively breaking the array in half by the largest value, 
//         if the previous condition is not true, since we are pushing the value
//         onto the back of the array, it must be on the right side.
            
//         OK, cool, so suppose the condition of val > curr node value is true.
//         Do we put the rest of the subtree on the left or right of the new node?
//         Note that it is impossible for the new node to have something to the 
//         right of it.  If so, that would imply it was not the rightmost node. 
            
//         So, we put it on the left side.
            
//         This was confusing for me to get without examples.
            
    
class Solution {
public:
    TreeNode* helper(TreeNode* root, int val){
        if(!root) return new TreeNode(val);
        if(val > root->val){
            TreeNode* ret = new TreeNode(val);
            ret->left = root;
            return ret;
        }
        else{
            root->right = helper(root->right, val);
            return root;
        }
    }
    
    TreeNode* insertIntoMaxTree(TreeNode* root, int val) {
        return helper(root, val);
    }
};
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


TreeNode* helper(TreeNode* root, int val){
    if(!root) return new TreeNode(val);
    if(val > root->val){
        TreeNode* ret = new TreeNode(val);
        ret->left = root;
        return ret;
    }
    else{
        root->right = helper(root->right, val);
        return root;
    }
}

TreeNode* insertIntoMaxTree(TreeNode* root, int val) {
    return helper(root, val);
}