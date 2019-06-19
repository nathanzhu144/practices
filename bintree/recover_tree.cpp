/*  Nathan Zhu, 11:06 am, Lunch break Amex building New York, NY
*   Recover binary search tree.
*
*   Two elements in a BST are swapped.  
*
*   Key insight here is an in-order traversal of the tree will reveal that two 
*   of the nodes are not in an increasing order.  We find those two, and swap the
*   values.
 */
#include <limits>

struct TreeNode {
     int val;
     TreeNode *left;
     TreeNode *right;
     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 };


TreeNode* first = nullptr;
TreeNode* second = nullptr;
TreeNode* prev = new TreeNode(INT_MIN);    //Tracks prev pointer in inorder traversal

//Helper function does an inorder traversal
void find_incorrect(TreeNode* curr){
    if(!curr){ return; }
    find_incorrect(curr->left);
    
    //We try to find first
    if(!first && curr->val < prev->val){
        first = prev;
    }
    //Once first is found, we can find second
    if(first && curr->val < prev->val){
        second = curr;
    }
    prev = curr;
    
    find_incorrect(curr->right);
}

void recoverTree(TreeNode* root) {
    //Find two incorrect nodes
    find_incorrect(root);

    //Swap the two values
    int temp = second->val;
    second->val = first->val;
    first->val = temp;
}
