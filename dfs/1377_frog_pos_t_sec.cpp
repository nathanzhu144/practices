
/**
 * Nathan Zhu May 21st, 2020.  Third day at Salesforce just finished!  I know my project now
 * Leetcode 1377 | hard | yeah kinda tricky
 * Category: DFS
 */

#include <set>
#include <vector>
#include <unordered_map>
#include <utility>

using namespace std;
// A couple strange edge cases:
// Since each edge is bidirectional, and the frog cannot jump backwards, we need to keep a visited set. 
// Since each edge is bidirectional, the number of nodes in each layer is always len(graph[curr] - 1), except for the top layer, which is len(graph[curr])
// the -1 comes from taking the reverse edge out, as we don't want to follow it.
//
// Since we end when graph[curr].size() == 1, but we have an edge case when target node == 1, since in that case graph[curr].size() == 0
// and it still should end the recursion, so we take care of that edge case in the main function.
//
//
// Oh yeah, general intuition for the function is we kinda do a weighted average with a dfs?
//
// Other cases: 
// If a frog goes past a node, it counts as not visiting it.
double helper(int curr, int target, int t, set<int> visited, unordered_map<int, vector<int>>& graph){
    if((graph[curr].size() == 1 && curr != 1) || t == 0) return (curr == target) ? 1 : 0;   // reach leaf node or time runs out, we stop
    double tot = 0;
    for(auto& neigh: graph[curr]){
        if(visited.count(neigh)) continue;
        visited.insert(neigh);
        tot += helper(neigh, target, t - 1, visited, graph);
    }
    int div = (curr == 1) ? graph[curr].size() : graph[curr].size() - 1;
    return tot / div;
}
double frogPosition(int n, vector<vector<int>>& edges, int t, int target) {
    unordered_map<int, vector<int>> graph;
    set<int> visited = {1};
    
    for(auto edge : edges){
        auto[n1, n2] = make_pair(edge[0], edge[1]);
        graph[n1].push_back(n2);
        graph[n2].push_back(n1);
    }
    if(target == 1 && graph[1].size() == 0) return 1;
    
    return helper(1, target, t, visited, graph);
}