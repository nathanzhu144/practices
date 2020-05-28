/* Nathan Zhu Sunday May 24th, 2020 Stockton, CA. I *think* I hit 1000 questions yesteray.
*  Leetcode 778 | hard | not too bad
*  Category: Djikstra
*            Can also be don with binary search or union find.
*/

#include <vector>
#include <set>
#include <utility>
#include <queue>
#include <tuple>
#include <algorithm>

using namespace std;

int swimInWater(vector<vector<int>>& grid) {
    vector<pair<int, int>> moves = {pair(1, 0), pair(0, 1), pair(-1, 0), pair(0, -1)};
    set<int> visited;
    if(!grid.size() or !grid[0].size()) return -1;   // should never happen.
    int R(grid.size()), C(grid[0].size());
    
    typedef tuple<int, int, int> triple;
    // Greater for "min pq"
    auto comp = [](triple& a, triple& b){
        return get<0>(a) > get<0>(b);
    };
    priority_queue<triple, vector<triple>, decltype(comp)> pq(comp);
    pq.emplace(grid[0][0], 0, 0);
    
    while(pq.size()){
        auto [dist, row, col] = pq.top(); pq.pop();
        if(row == R - 1 && col == C - 1) return dist;
        for(auto [dr, dc] : moves){
            int newr(dr + row), newc(dc + col);
            int calc = newr * C + newc;
            if(newr < 0 or newc < 0 or newr >= R or newc >= C or visited.count(calc)) continue;
            visited.insert(calc);
            pq.emplace(max(dist, grid[newr][newc]), newr, newc);;
        }
    }
    
    return -1;
    
}