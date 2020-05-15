/*  Nathan Zhu April 13th, 2020.
*   Leetcode 1391 | medium | kinda hard for a med
*   Category: DFS
*
*   We have to be smart in how we follow the path, we need to take into 
*   account direction
*/

#include <vector>
#include <utility>
#include <unordered_map>

using namespace std;

// Maps prev direction -> new direciton.
// 
//             up(3)
//         ------------
// left(1) |          | right(0)
//         |          |
//          -----------
//            down(2)
//
vector<pair<int, int>> dirs = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

// These represent direction changes.
vector<unordered_map<int, int>> states = {{},
                                            {{1,1},{0, 0}},
                                            {{3,3},{2,2}},
                                            {{0,2},{3,1}},    // Ex. right -> down or up -> left
                                            {{3,0},{1,2}},
                                            {{0,3},{2,1}},
                                            {{2,0},{1,3}}
                                            };

bool helper(vector<vector<int>>&grid, int dir){
    int R(grid.size()), C(grid[0].size()), r(0), c(0);
    
    while(r >= 0 and c >= 0 and r < R and c < C){
        int type = grid[r][c];
        
        if(states[type].count(dir) == 0) return false;       // order of these two checks matter
        if(r == R - 1 and c == C - 1) return true;           // we want to make sure road on destination square connects with path
        auto nextdir = states[type][dir];
        auto [dr, dc] = dirs[nextdir];
        int newr(r + dr), newc(c + dc);
        dir = nextdir;
        c = newc; r = newr;
        if(newr == 0 and newc == 0) return false; // exists cycle
    }
    
    return false;
}
bool hasValidPath(vector<vector<int>>& grid) {
    return helper(grid, 0) or helper(grid, 1) or helper(grid, 2) or helper(grid, 3);
}