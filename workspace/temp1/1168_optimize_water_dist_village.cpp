/* Nathan Zhu Saturday Stockton, CA, 1:49 am June 20th, 2020.  Day off on Friday yesterday
*  Leetcode 1168 | hard | hard
*  Category: Kruskal + UF
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

class UF{
public:
    void try_make(int x){
        if(!parent.count(x)) parent[x] = x;
    }
    
    int find(int x){
        if(parent[x] != x) parent[x] = find(parent[x]);
        return parent[x];
    }
    
    bool join(int a, int b){
        auto p1(find(a)), p2(find(b));
        if(p1 == p2) return false;
        parent[p1] = p2;
        return true;
    }
private:
    unordered_map<int, int> parent;
};

int minCostToSupplyWater(int n, vector<int>& wells, vector<vector<int>>& pipes) {
    int N(wells.size()), ret(0);
    auto u = UF();
    
    for(int i = 0; i < N; ++i){
        pipes.push_back({0, i + 1, wells[i]});
    }
    
    sort(begin(pipes), end(pipes), [](auto& v1, auto& v2){ return v1[2] < v2[2]; });
    for(auto& vec: pipes){
        auto from(vec[0]), to(vec[1]), cost(vec[2]);
        u.try_make(from);
        u.try_make(to);
        auto p1(u.find(from)), p2(u.find(to));
        if(p1 == p2) continue;
        u.join(p1, p2);
        ret += cost;
    }
    
    return ret;
}
