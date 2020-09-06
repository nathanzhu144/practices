/* Nathan Zhu Friday Stockton, CA. 10:41 pm June 19th, 2020.  Day off on Friday today. :)
*  Leetcode 285 | medium | medium
*  Category: tree
*/

#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <set>
#include <string>
#include <stack>
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
// Two cases:
// This soln relies on unique values in tree & p actuall being in the tree.
// 1. Inorder successor is "beneath" the node p. 
//    To get inorder successor, from node p we go right, then go as far left as we can.
// 2. Inorder successor is not beneath node p. 
//    When we are finding p, it is the last node in our traversal >= p value.
//    So, we don't actually need a stack; the stack is only useful if we need to find the kth
//    inorder successor.
TreeNode* inorderSuccessor(TreeNode* root, TreeNode* p) {
    stack<TreeNode*> post;
    TreeNode* curr = root;
    
    while(curr->val != p->val){
        if(curr->val < p->val){
            curr = curr->right;
        }
        else{
            post.push(curr);
            curr = curr->left;
        }
    }
    
    // no successor
    if(!curr->right && !post.size()) return nullptr;
    // successor is not beneath p
    else if(!curr->right && post.size()) return post.top();
    // successor is "beneath" p
    else if(curr->right){
        curr = curr->right;
        while(curr->left) curr = curr->left;
        return curr;
    }
    
    return nullptr;
}