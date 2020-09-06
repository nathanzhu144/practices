
/* Nathan Zhu  Saturday July 18th, 2020  11:57 am Had to cancel hot pot with Tan, Hiro, and co for today.  Coronavirus ya know? 
*  Leetcode 1361 | medium | tricky
*  Category: tree
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




// I'm using definition of binary tree as a minimally connected graph.
// If we have a graph with n nodes and n - 1 edges, and the graph is connected,
// it should be a tree.  (a minimally connected graph).
//
// We check to see if there are multiple roots.  
// If there is only a single root, and n - 1 edges, we can safely do a dfs from that root, and not
// worry about cycles.  The idea is that since each node besides the root has one incoming edge, 
// and we have n - 1 edges in total, there is no cycle besides possible nodes pointing to themselves.
// 
//
// Note this function doesn't handle cycles.
int count(int root, vector<int>& left, vector<int>& right){
    if(root == -1) return 0;
    return 1 + count(left[root], left, right) + count(right[root], left, right);
}

bool validateBinaryTreeNodes(int n, vector<int>& leftchild, vector<int>& rightchild) {
    // Definition of binary tree
    // From minimal connected graph.  
    // Acyclic connected graph
    // From each node, to any other node is a connection.
    vector<int> indegree(n, 0);
    
    for(int i = 0; i < n; ++i){
        if(leftchild[i] != -1) indegree[leftchild[i]]++;
        if(rightchild[i] != -1) indegree[rightchild[i]]++;
    }
    
    
    // find root, and count indegrees.
    int root = -1;
    int indegrees = 0;
    for(int i = 0; i < n; ++i){
        indegrees += indegree[i];         // any indegree > 1 cannot be minimally connected
        if(indegree[i] == 0){
            if(root != -1) return false;  // multiple roots
            root = i;                     // this is root
        }
    }
    if(root == -1) return false;          // root cannot be found
    
    return (indegrees == n - 1 && count(root, leftchild, rightchild) == n) ? true : false;
}
