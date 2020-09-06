/* Nathan Zhu Friday 12:36 am, June 19th, 2020.  Yesterday is our 2nd anniversary. :)  50.24% of leetcode questions done.  Called everyone today
*                                                               Dom, Katelyn, Catherine, Amber, Wendy etc, etc. Good seeing everyone again.  Everyone's changed so much you know?  
*  Leetcode  815 | hard | hard
*  Category: BFS
*/


#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <set>
#include <string>
#include <queue>
#include <deque>
#include <utility>
#include <algorithm>
#include <cmath>
#include <limits>
#include <iostream>

using namespace std;

int numBusesToDestination(vector<vector<int>>& routes, int S, int T) {
    unordered_map<int, vector<int>> to_bus;
    unordered_set<int> visited_routes, visited_nodes;
    
    // For each node in graph, which routes can it go to?
    for(int stop = 0; stop < routes.size(); ++stop){
        for(auto node : routes[stop]) to_bus[node].push_back(stop);
    }
    
    queue<int> q;
    q.push(S);
    int ret = 0;
    while(q.size()){
        int size = q.size();
        while(size--){
            int curr = q.front(); q.pop();
            if(curr == T) return ret;                       // found target
            for(auto route: to_bus[curr]){
                if(visited_routes.count(route)) continue;   // don't revisit any "route"
                visited_routes.insert(route);
                for(auto node : routes[route]){
                    if(visited_nodes.count(node)) continue;  // don't revisit any "stop"
                    visited_nodes.insert(node);
                    q.push(node);
                }
            }  
        }
        ++ret;
    }
    return -1;
}