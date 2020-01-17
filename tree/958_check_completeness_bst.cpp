// Nathan Zhu Saturday Sept 21st, 2019 12:06 pm
// Category: BFS / tree
//
// Given a binary tree, determine if it is a complete binary tree.

// Definition of a complete binary tree from Wikipedia:
// In a complete binary tree every level, except possibly the last, is completely 
// filled, and all nodes in the last level are as far left as possible.
// It can have between 1 and 2h nodes inclusive at the last level h.
 
 #include <vector>

 using namespace std;
 
 
 struct TreeNode {
     int val;
     TreeNode *left;
     TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 };

// If a tree is complete, when we first see a nullptr in our queue, all elements after that must be nullptrs.
bool isCompleteTree(TreeNode* root) {
    vector<TreeNode*> q = {root};
    
    int i = 0;
    //keep adding to queue until we find our first nullptr
    while(i < q.size() && q[i]){
        q.push_back(q[i]->left);
        q.push_back(q[i]->right);
        ++i;
    }
    
    //check if all things in q after our nullptr are nullptrs
    while(i < q.size() && !q[i]) ++i;
    return i == q.size();
}