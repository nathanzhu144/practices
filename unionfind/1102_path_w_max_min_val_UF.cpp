/* Nathan Zhu April 9th, 2020 Stockton, CA. 
*  Leetcode 1102 | medium | damn this soln is cool
*
*  Sort from biggest to smallest sqare, then call union find from biggest to
*  smallest square. Return the value at which {0, 0}, {R - 1, C - 1} share
*  same parent.
*/

#include <algorithm>
#include <string>
#include <vector>
#include <unordered_map>
#include <tuple>
using namespace std;
class UF{
public:
    UF(){}
    
    int get_min(string x) { return graph_to_min[find(x)]; }
    bool exists(string x) { return parent.count(x); }
    string make_coord(pair<int, int> x) { return to_string(x.first) + " " + to_string(x.second); }
    
    void touch(string x, int val){
        parent[x] = x;
        graph_to_min[x] = val;
    }
        
    string find(string x){
        if(parent[x] != x) parent[x] = find(parent[x]);
        return parent[x];
    }
    
    void combine(string a, string b){
        auto p1(find(a)), p2(find(b));
        if(p1 == p2) return;
            
        // we choose p1 to be new represt of combined graph
        parent[p2] = p1;
        graph_to_min[p1] = min(graph_to_min[p1], graph_to_min[p2]);
        graph_to_min.erase(p2);
    }
    private:
    unordered_map<string, string> parent;
    unordered_map<string, int> graph_to_min;
};

class Solution {
public:
    int maximumMinimumPath(vector<vector<int>>& A) {
        vector<tuple<int, int, int>> grid_vals;
        if(!A.size() or !A[0].size()) return 0; // return 0 if empty graph
        int R(A.size()), C(A[0].size());
        
        for(int r = 0; r < R; ++r){
            for(int c = 0; c < C; ++c){
                grid_vals.push_back({r, c, A[r][c]});
            }
        }
    
    
        sort(grid_vals.begin(), grid_vals.end(), [](tuple<int, int, int> a, tuple<int, int, int> b)
             { return get<2>(a) > get<2>(b); });

        UF uf;
        auto start(uf.make_coord({0, 0})), end(uf.make_coord({R - 1, C - 1}));
        for(auto& tup : grid_vals){
            auto [r, c, val] = tup;
            auto coord = uf.make_coord({r, c});
            uf.touch(coord, val);
            vector<pair<int, int>> moves = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
            for(auto& [dr, dc] : moves){
                int newr(dr + r), newc(dc + c);
                auto newcoord = uf.make_coord({newr, newc});
                if(uf.exists(newcoord)) uf.combine(newcoord, coord);
                if(uf.exists(start) and uf.exists(end) and uf.find(start) == uf.find(end)) return uf.get_min(coord);
            }
        }
        return -1;
    }
};