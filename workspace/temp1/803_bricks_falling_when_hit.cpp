/* Nathan Zhu Monday Stockton, CA. 12:52 am June 22nd, 2020.  I watched a william lin video of him doing 150 questions in 12 hours lol.  OK my dude.
*  Leetcode 803 | hard | hard
*  Category:  Union find
*
*  This question is like the opposite of number islands II.  
*  Instead of joining squares iteratively as squares come along, we go backwards.
*  We first color all squares that will be erased (and are not already empty) as 2, to distingish them from the 1s.
*
*  (Note that position 0 in our uf actually represents whole top row)
*  Then, we count how many squares are joined to the ceiling by checking uf.size[uf.find(0)]
*  For each square from last to first, we change the square from 2 to 1 (or do nothing if it is 0)
*  and then join against the four surrounding sq if they are 1, and count the new number of squares joined
*  to the ceiling.
*
*  Pretty challenging
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

class UF{
public:
    UF(int N){
        parent = vector<int>(N, 0);
        size = vector<int>(N, 1);
        for(int i = 0; i < N; ++i){
            parent[i] = i;
        }
    }
    
    int find(int a){
        if(parent[a] != a) parent[a] = find(parent[a]);
        return parent[a];
    }
    
    bool join(int a, int b){
        int p1(find(a)), p2(find(b));
        if(p1 == p2) return false;
        size[p1] += size[p2];
        parent[p2] = p1;
        return true;
    }

    vector<int> parent;
    vector<int> size;
};



class Solution {
public:
    int mark(int C, int r, int c){
        return 1 + r * C + c;
    }
    
    void join_surrounding(vector<vector<int>>& grid, UF& u, int r, int c){
        int R(grid.size()), C(grid[0].size());
        int curr_hash = mark(grid[0].size(), r, c);
        vector<pair<int, int>> changes = {pair(1, 0), pair(-1, 0), pair(0, 1), pair(0, -1)};
        
        for(auto [dr, dc] : changes){
            int newr(dr + r), newc(dc + c);
            if(newr >= 0 && newc >= 0 && newr < R && newc < C && grid[newr][newc] == 1){
                int new_hash = mark(grid[0].size(), newr, newc);
                u.join(curr_hash, new_hash);
            }
        }
        
        if(r == 0) u.join(curr_hash, 0);
    }
    
    vector<int> hitBricks(vector<vector<int>>& grid, vector<vector<int>>& hits) {
        if(!grid.size() || !grid[0].size()) return {};
        
        int R(grid.size()), C(grid[0].size());
        UF u(R * C + 1);               // Spot 0 in our UF is specifically for first row.
        int N(hits.size());
        vector<int> ret(N, 0);
        
        // Mark all hit squares as 2 (Note we only mark squares previously 1)
        for(const auto& vec: hits){
            int r(vec[0]), c(vec[1]);
            if(grid[r][c] == 1) grid[r][c] = 2;
        }
        
        for(int r = 0; r < R; ++r){
            for(int c = 0; c < C; ++c){
                if(grid[r][c] == 1) join_surrounding(grid, u, r, c);
            }
        }
        
        int last_supported = u.size[u.find(0)];
        for(int i = N - 1; i >= 0; i--){
            int r(hits[i][0]), c(hits[i][1]);
            if(grid[r][c] != 2) continue;  // erased empty brick
            grid[r][c] = 1;
            join_surrounding(grid, u, r, c);
            int curr_supported = u.size[u.find(0)];
            ret[i] = max(0, curr_supported - last_supported - 1);  // +1 is to exclude brick erased
            last_supported = curr_supported;
        }
        
        return ret;
    }
};