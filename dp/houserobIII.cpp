/*
 * Nathan Zhu, 9:18 am American Express Tower 
 * So, the robber this time finds a bunch of houses that are connected in a binary
 * search tree.  If the robber robs any houses that are connected, the police get called.
 * 
 * Base case:
 *    house_rob_3(nullptr) is 0
 * 
 * Inductive step:
 *               
 * 
 * Ex.       A
 *         /  \
 *        B    C
 *       / \   / \
 *      D  E  F   G
 * 
 *   Assuming the children of A have (B and C) have children themselves (D E F G), then
 *   the robber can either rob A, and potentially rob D E F G OR the robber can decide not to rob
 *   A and potentially rob B and C.
 * 
 *   Therefore, assuming B and C exist for A, 
 * 
 *       helper(root) = MAX((root->val + helper(root->left->left) + helper(root->left->right)
 *                                     + helper(root->right->left + helper(root->right->right)),
 *                           helper(root->left) + helper(root->right))
 * 
 * 
*/

#include <vector>
#include <unordered_map>

using namespace std;

 struct TreeNode {
      int val;
      TreeNode *left;
      TreeNode *right;
      TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 };


 long helper(TreeNode* root, unordered_map<TreeNode*, long>& mem){
    long left_child_childs_sum = 0;
    long right_child_childs_sum = 0;
        
    if (mem.count(root) != 0){ return mem[root]; }
        
    if(root == nullptr) { return 0; }
        
    if(root->left != nullptr){
        left_child_childs_sum = helper(root->left->left, mem) + helper(root->left->right, mem);
    }
        
    if(root->right != nullptr){
        right_child_childs_sum = helper(root->right->left, mem) + helper(root->right->right, mem);
    }
    
    mem[root] = std::max(root->val + left_child_childs_sum + right_child_childs_sum,
                        helper(root->left, mem) + helper(root->right, mem));
    
    return mem[root];
}
                             
                             
int house_robber_III(TreeNode* root) { 
    unordered_map<TreeNode*, long> mem;
    return helper(root, mem);
}

