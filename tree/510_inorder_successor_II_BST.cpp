/* Nathan Zhu May 17th, 2020  Starting at Salesforce tomorrow!
*  Leetcode 510 | medium | medium
*  Category: Binary tree
*
*  The followup where you do it without looking at node values in tree is sick man.
*/



class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* parent;
};

Node* inorderSuccessor(Node* node) {
    if(!node) return node;
    if(node->right){
        auto ret = node->right;
        while(ret->left) ret = ret->left;
        return ret;
    }
    // This part didn't make sense to me, I originally was thinking of just looking at the parent.
    // However, there are some cases, where this node is on the right, that this node has a bigger value
    // than the parent.  Thus, we can just walk until we get to a parent which has a bigger value than node.
    else{
        while(node->parent and node->parent->val < node->val){
            node = node->parent;
        }
        return node->parent;
    }
}

// Doing it without looking at the values in the tree.
Node* inorderSuccessorFollowup(Node* node) {
    if(!node) return node;
    if(node->right){
        auto ret = node->right;
        while(ret->left) ret = ret->left;
        return ret;
    }
    // This part didn't make sense to me, I originally was thinking of just looking at the parent.
    // However, there are some cases, where this node is on the right, that this node has a bigger value
    // than the parent.  Thus, we can just walk until we get to a parent which has a bigger value than node.
    else{
        while(node->parent){
            auto parent = node->parent;
            if(parent->right != node) return parent;
            node = node->parent;
        }
    }
    return nullptr;
}