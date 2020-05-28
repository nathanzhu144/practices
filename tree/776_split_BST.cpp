/** May 10th, 2020, Stockton, CA.  First day at work, 10:54 pm.  We did mostly orientations today, but first day at work!!
 *  Leetcode 776 | medium | medium
 *  Category: Tree
 *  Runtime O(N), space O(N)
 * 
 *  THERE'S A WAY TO DO THIS IN O(H) SPACE WITHOUT A COPY. FIGURE THAT OUT TOMORROW.
 * 
 *  Honestly, it feels like everything is coming full-circle.  It was more or less two weeks to the day that I start work in New York.  It was three days ago when
 *  we had our trip in california with Hershal and crew.  It was before work on that first day at Amex that I really started doing leetcode.  I think I started from
 *  maybe 30 questions done or something?  I was laughably bad, but at some point since I always did leetcode at lunch, everyone came to think I was pretty good.  
 * 
 *  I haven't comped the latest couple days, but I'm definitely within hitting range of doing 1000 questions total this year.  My counter says 939 not including the work of the last 
 *  3 days, and there was one day where I did at least 10 questions.  If I can do 50 questions in the next two weeks, I can hit 1000 qs done.  That's damn doable, and 
 *  I can get that done.
 * 
 */



#include <unordered_map>
#include <vector>
using namespace std;


class TreeNode {
public:
    TreeNode(int n){ val = n; }
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode* parent;
};


TreeNode* copy(TreeNode* n){
    if(!n) return n;
    TreeNode* cpy = new TreeNode(n->val);
    cpy->left = copy(n->left);
    cpy->right = copy(n->right);
    return cpy;
}

// Does not mutate tree's root, instead returns a copy of the tree with all
// nodes <= val.
// Runs in O(N) time instead of O(h)
TreeNode* make_smaller(TreeNode* root, int val){
    if(!root) return nullptr;

    // Note: If right is OK, root is OK TOO, we don't need to consider
    if(root->val <= val){
        TreeNode *cpy = new TreeNode(root->val);
        cpy->left = copy(root->left);
        cpy->right = make_smaller(root->right, val);
        return cpy;
    }
    // If root is NOT OK, right is NOT Ok, only possible valid nodes are on left.
    else {
        return make_smaller(root->left, val);
    }
}

// Does mutate tree. Returns tree with all nodes > val.
TreeNode* make_bigger(TreeNode* root, int val){
    if(!root) return root;
    
    // Note: If left is OK, root must be OK TOO, so we don't consider a case for that.
    if(root->val > val){
        root->left = make_bigger(root->left, val);
        return root;
    }
    else return make_bigger(root->right, val);
}
vector<TreeNode*> splitBST(TreeNode* root, int V) {
    TreeNode* smaller = make_smaller(root, V);
    TreeNode* bigger = make_bigger(root, V);
    return {smaller, bigger};
}