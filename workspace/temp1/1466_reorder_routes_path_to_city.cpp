/* Nathan Zhu Stockton, CA, June 1st, 2020. 8:18 ams Tomorrow is the first day I start at Amex last year! :O
*  Leetcode 1466 | medium | kinda hard?? lol
*  Category: DFS
*
*  Tricks: To track direction of a node, I set it to negative of its original value if it is facing the other direction
*          Then, just do a DFS from node 0 to rest of nodes, with a visited set.
*/

#include <unordered_map>
#include <vector>
using namespace std;

int dfs(int from, vector<bool>& visited, unordered_map<int, vector<int>>& graph){
    int ret = 0;
    visited[from] = true;
    for(auto to: graph[from]){
        if(!visited[abs(to)]){
            ret += dfs(abs(to), visited, graph) + int(to > 0);
        }
    }
    return ret;
}
int minReorder(int n, vector<vector<int>>& connections) {
    unordered_map<int, vector<int>> table;
    for(auto& c: connections){
        table[c[0]].push_back(c[1]);
        table[c[1]].push_back(-c[0]);
    }
    return dfs(0, vector<bool>(n) = {}, table);
}