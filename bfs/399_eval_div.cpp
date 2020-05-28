/*  Nathan Zhu May 20th, 2020 3rd day of work at Salesforce!
*   Leetcode 399 | medium | kinda harder for a medium
*   Category: BFS
*   So, you see the divisons as a graph...
*
*   Note: [a/b = 2 and b/c = 3] means a/b * b/c = a/c = 6
*/

#include <string>
#include <unordered_map>
#include <vector>
#include <set>
#include <utility>
#include <algorithm>
using namespace std;

double bfs(string& start, string& end, unordered_map<string, vector<pair<string, double>>> graph){
    if(!graph.count(start) || !graph.count(end)) return -1.0;
    
    vector<pair<string, double>> q = {{start, 1.0}};
    set<string> visited = {start};
    
    while(q.size()){
        vector<pair<string, double>> newq;
        
        for(auto& [node, prod] : q){
            if(node == end) return prod;
            for(auto& [neigh, val] : graph[node]){
                if(visited.count(neigh)) continue;
                visited.insert(neigh);
                newq.push_back(pair{neigh, val * prod});
            }
        }
        q.clear();
        move(newq.begin(), newq.end(), back_inserter(q));
    }
    return -1.0;
    
}

vector<double> calcEquation(vector<vector<string>>& equations, vector<double>& values, vector<vector<string>>& queries) {
    unordered_map<string, vector<pair<string, double>>> graph;
    vector<double> ret;
    
    for(int i = 0; i < equations.size(); ++i){
        auto [num, denom] = pair{equations[i][0], equations[i][1]};
        double val = values[i];
        graph[num].push_back(pair{denom, val});
        graph[denom].push_back(pair{num, 1 / val});
    }
    
    for(auto query: queries){
        auto [s, e] = pair{query[0], query[1]};
        ret.push_back(bfs(s, e, graph));
    }
    
    return ret;
}