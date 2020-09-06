/* Nathan Zhu Tuesday July 14th, 2020  Stockton, CA. TACO TUESDAY
*  Deploying golang projects to Heroku is really fun.  :P
*  Leetcode 1490 | medium | EZ
*  Category: tree\]'
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



class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};

Node* cloneTree(Node* root) {
    if(!root) return nullptr;
    Node* ret = new Node(root->val);
    for(auto child : root->children){
        ret->children.push_back(cloneTree(child));
    }
    return ret;
}