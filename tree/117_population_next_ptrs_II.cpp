/* Nathan Zhu May 9th, 2020 Damn this is cool, I like this problem.
*  Leetcode 117 | medium | kinda hard?
*  Category: Modified BFS on binary tree
*
*  So, we are NOT allowed to use extra space.  So, we use each level
*  of the tree as an implict queue in the BFS.  
*
*  In each level, make a dummy head, and then we connect the next pointers
*  in the level right below the current level.  Since the bST is not necessarily
*  complete, we have to manually look for the next pointer to connect.
*
*  Another challenge I really struggled on is, after connecting the next level,
*  How do I know where the leftmost node is in the next level?
*  Easy, just do dummynode->next.  
*
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


class Solution {
public:
    Node* connect(Node* root) {
        for(Node* curr = root; curr; ){
            Node* false_lvl_head = new Node(0);
            Node* prev = false_lvl_head;
            
            for(Node* levelcurr = curr; levelcurr; levelcurr = levelcurr->next){
                if(levelcurr->left){
                    prev->next = levelcurr->left;
                    prev = levelcurr->left;
                }
                if(levelcurr->right){
                    prev->next = levelcurr->right;
                    prev = levelcurr->right;
                }
            }
            
            curr = false_lvl_head->next;
        }
        return root;
    }
};