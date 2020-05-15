/* Nathan Zhu May 9th, 2020. Think I just need to do this with BFS
*  Leetcode 200 | medium | nice
*  Category: DFS
*
*/
#include <vector>
#include <tuple>
#include <stack>

using namespace std;

int numIslands(vector<vector<char>>& grid) {
    if(!grid.size() or !grid[0].size()) return 0;
    int R(grid.size()), C(grid[0].size());
    int ret = 0;
    
    for(int r = 0; r < R; ++r){
        for(int c = 0; c < C; ++c){
            if(grid[r][c] == '1'){
                ret++;
                stack<pair<int, int>> stk;
                stk.push({r, c});
                
                while(stk.size()){
                    auto [cr, cc] = stk.top(); stk.pop();
                    
                    vector<tuple<int, int>> change = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
                    for(auto [dr, dc] : change){
                        int newr(cr + dr), newc(cc + dc);
                        if(0 <= newr and newr < R and 0 <= newc and newc < C and grid[newr][newc] == '1'){
                            grid[newr][newc] = '0';
                            stk.emplace(newr, newc);
                        }
                    }
                }
            }
        }
    }
    
    return ret;
}