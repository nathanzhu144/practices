/* Nathan Zhu  Monday July 20th, 2020 5:30 pm Stockton, CA.  Emailed Katie & Jaewon today.
*  Leetcode 1345 | hard | medium
*  Category: BFS with some smartness
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



int minJumps(vector<int>& arr) {
    queue<int> q;
    q.push(0);
    unordered_map<int, vector<int>> same;
    unordered_set<int> visited;
    int N(arr.size()), ret(0), target(arr.size() - 1);
    
    for(int i = 0; i < N; ++i) same[arr[i]].push_back(i);
    
    while(q.size()){
        int currsize = q.size();
        while(currsize--){
            int curr = q.front(); q.pop();
            if(curr == target) return ret;
            vector<int>& cand = same[arr[curr]];
            cand.push_back(curr - 1);
            cand.push_back(curr + 1);
            
            for(auto idx: cand){
                if(idx < 0 || idx >= N || visited.count(idx)) continue;
                visited.insert(idx);
                q.push(idx);
            }
            
            cand.clear();  // don't want to re-traverse this value again.
        }
        ++ret;
    }
    
    return -1;
}