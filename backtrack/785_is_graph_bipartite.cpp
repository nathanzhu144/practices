/** Nathan Zhu Thursday March 19th, 2020, 9:55 pm. 
 *  Leetcode 785 | medium | medium
 *  Category: Backtracking
 * 
 *  
 */

#include <vector>

using namespace std;

bool dfs(int node, int color, vector<vector<int>>& graph, vector<int>& colors){
    if(colors[node]) return color == colors[node];
    
    colors[node] = color;
    
    int next = (color == 1) ? 2 : 1;
    
    for(int i = 0; i < graph[node].size(); ++i){
        if(!dfs(graph[node][i], next, graph, colors)) return false;
    }
    return true;
}

// In colors,
// color == 0 unvisited
//          1 red
//          2 black
bool isBipartite(vector<vector<int>>& graph) {
    int size = graph.size();
    vector<int> colors(size, 0);
    
    for(int i = 0; i < size; ++i){
        if(colors[i] == 0 and !dfs(i, 1, graph, colors)) return false;
    }
    return true;
}