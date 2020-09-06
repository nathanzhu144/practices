/* Nathan Zhu Thursday Stockton, CA. 5:43, pm June 18th, 2020.  Tomorrow is our 2nd anniversary. :)  50.24% of leetcode questions done.  Called everyone today
*                                                               Dom, Katelyn, Catherine, Amber, Wendy etc, etc. Good seeing everyone again.  Everyone's changed so much you know?  
*  Leetcode 993 | easy | medium
*  Category: BFS
*/


#include <vector>
#include <unordered_map>
#include <set>
#include <string>
#include <unordered_set>
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
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};


bool isCousins(TreeNode* root, int x, int y) {
    if(x > y) return isCousins(root, y, x);  // guarantees x <= y
    
    queue<TreeNode*> q; 
    q.push(root);
    while(q.size()){
        int n = q.size();
        unordered_set<int> level;
        while(n--){
            TreeNode* curr = q.front(); q.pop();
            level.insert(curr->val);
            // adding children to back of q
            if(curr->left) q.push(curr->left);
            if(curr->right) q.push(curr->right);
            
            // same parent check
            if(curr->left && curr->right){
                auto [lval, rval] = pair(curr->left->val, curr->right->val);
                if(min(lval, rval) == x && max(lval, rval) == y) return false;
            }
        }
        // Nodes are unique, so if any of the two are found on this level, both must be found on this lvl
        if(level.count(x) || level.count(y)) return level.count(x) && level.count(y);
    }
    
    return false;
}