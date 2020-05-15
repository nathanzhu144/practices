/* Nathan Zhu May 9th, 2020 Damn this is cool, I like this problem.
*  Leetcode 116 | medium | okish
*  Category: binary tree
*
*  So, Leetcode 117 gives the more general soln, but this works only for a complete
*  BST. 
*  
*  We connect the previous level, before using the next pointer we connected before to 
*  another level.
*/



class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() : val(0), left(nullptr), right(nullptr), next(nullptr) {}

    Node(int _val) : val(_val), left(nullptr), right(nullptr), next(nullptr) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};


Node* connect(Node* root) {
    if(!root) return root;
    if(root->left) root->left->next = root->right;
    if(root->right) root->right->next = (!root->next) ? nullptr : root->next->left;
    connect(root->left);
    connect(root->right);
    return root;
}