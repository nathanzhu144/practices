/* Nathan Zhu Tuesday, Stockton, CA. 6:51 pm, June 16th, 2020 Called Sophie from Amex today.
*  Leetcode 1219 | medium | EZ
*  Category: DFS
*/
#include <vector>
using namespace std;
int dfs(vector<vector<int>>& grid, int r, int c){
    if(r < 0 || c < 0 || r >= grid.size() || c >= grid[0].size() || grid[r][c] == 0) return 0;
    int ret = grid[r][c];
    grid[r][c] = 0;
    int one = dfs(grid, r + 1, c);
    int two = dfs(grid, r - 1, c);
    int three = dfs(grid, r, c + 1);
    int four = dfs(grid, r, c - 1);
    grid[r][c] = ret;
    
    return ret + max(max(one, two), max(three, four));
}

int getMaximumGold(vector<vector<int>>& grid) {
    if(!grid.size() || !grid[0].size()) return 0;
    int R(grid.size()), C(grid[0].size());
    int ret = 0;
    
    for(int r = 0; r < R; ++r){
        for(int c = 0; c < C; ++c){
            ret = max(ret, dfs(grid, r, c));
        }
    }
    return ret;
}