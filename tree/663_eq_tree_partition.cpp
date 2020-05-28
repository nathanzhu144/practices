/** May 10th, 2020, Stockton, CA.  First day at work, 7:21 pm.  We did mostly orientations today, but first day at work!!
 *  Leetcode 663 | medium | medium
 *  Category: Tree
 *  Runtime O(N), space O(N)
 *  Honestly, it feels like everything is coming full-circle.  It was more or less two weeks to the day that I start work in New York.  It was three days ago when
 *  we had our trip in california with Hershal and crew.  It was before work on that first day at Amex that I really started doing leetcode.  I think I started from
 *  maybe 30 questions done or something?  I was laughably bad, but at some point since I always did leetcode at lunch, everyone came to think I was pretty good.  
 * 
 *  I haven't comped the latest couple days, but I'm definitely within hitting range of doing 1000 questions total this year.  My counter says 939 not including the work of the last 
 *  3 days, and there was one day where I did at least 10 questions.  If I can do 50 questions in the next two weeks, I can hit 1000 qs done.  That's damn doable, and 
 *  I can get that done.
 */


#include <unordered_map>
using namespace std;

//          0
//         /  |
//       -1   1
// be careful of this case.

class TreeNode {
public:
    TreeNode(int n){ val = n; }
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode* parent;
};

int find_heights(TreeNode* root, unordered_map<TreeNode*, int>& table){
    if(!root) return 0;
    table[root] = root->val + find_heights(root->left, table) + find_heights(root->right, table);
    return table[root];
}

bool helper(TreeNode* root, int tot, unordered_map<TreeNode*, int>& table){
    if(!root) return false;
    if(table[root] == tot / 2) return true;
    else return helper(root->left, tot, table) || helper(root->right, tot, table);
}

bool checkEqualTree(TreeNode* root) {
    unordered_map<TreeNode*, int> table;
    
    find_heights(root, table);
    return (table[root] % 2 == 0) && (helper(root->left, table[root], table) || helper(root->right, table[root], table));  // we need two recursive calls to helper to avoid that case
}