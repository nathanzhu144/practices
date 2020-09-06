/* Nathan Zhu Tuesday July 14th, 2020  Stockton, CA. TACO TUESDAY
*  Deploying golang projects to Heroku is really fun.  :P
*  Leetcode 729 | medium | medi
*  Category: Design
*/


#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <set>
#include <stack>
#include <string>
#include <queue>
#include <deque>
#include <utility>
#include <algorithm>
#include <cmath>
#include <limits>
#include <iostream>

using namespace std;

struct NodeCopy{
    NodeCopy(int x) : val(x), left(nullptr), right(nullptr), random(nullptr) {}
    int val;
    NodeCopy* left;
    NodeCopy* right;
    NodeCopy* random;
};

struct Node{
    Node(int x) : val(x), left(nullptr), right(nullptr), random(nullptr) {}
    int val;
    Node* left;
    Node* right;
    Node* random;
};

void dfs(Node* root, unordered_map<Node*, NodeCopy*>& old_to_new){
    if(!root) return;
    old_to_new[root] = new NodeCopy(root->val);
    dfs(root->left, old_to_new);
    dfs(root->right, old_to_new);
}

void connect(Node* root, unordered_map<Node*, NodeCopy*>& old_to_new){
    if(!root) return;
    if(root->left) old_to_new[root]->left = old_to_new[root->left];
    if(root->right) old_to_new[root]->right = old_to_new[root->right];
    if(root->random) old_to_new[root]->random = old_to_new[root->random];
    
    connect(root->left, old_to_new);
    connect(root->right, old_to_new);
}

NodeCopy* copyRandomBinaryTree(Node* root) {
    unordered_map<Node*, NodeCopy*> old_to_new;
    
    dfs(root, old_to_new);
    connect(root, old_to_new);
    return old_to_new[root];
}