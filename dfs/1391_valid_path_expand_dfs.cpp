/*  Nathan Zhu April 13th, 2020.
*   Leetcode 1391 | medium | kinda hard for a med
*   Category: expand DFS, similar to number regions divided by slashes.
*
*/

#include <vector>
using namespace std;

bool follow(vector<vector<bool>>& grid, int r, int c){
    int R(grid.size()), C(grid[0].size());
    if(r < 0 or c < 0 or r >= R or c >= C or !grid[r][c]) return false;
    if(r == R - 2 and c == C - 2) return true;
    grid[r][c] = false;           // prevent inf backtracking
    return follow(grid, r + 1, c) or follow(grid, r, c + 1) or follow(grid, r - 1, c) or follow(grid, r, c - 1);
}
bool hasValidPath(vector<vector<int>>& grid) {
    int R(grid.size()), C(grid[0].size());
    
    vector<vector<bool>> ngrid(R * 3, vector<bool>(C * 3, false));
    // Expand grid by 3x, and then follow path
    for(int r = 0; r < R; ++r){
        for(int c = 0; c < C; ++c){
            auto type = grid[r][c];
            ngrid[3 * r + 1][3 * c + 1] = true;
            ngrid[3 * r + 1][3 * c] = (type == 1 or type == 3 or type == 5);
            ngrid[3 * r][3 * c + 1] = type == 2 or type == 5 or type == 6;
            ngrid[3 * r + 2][3 * c + 1] = type == 2 or type == 3 or type == 4;
            ngrid[3 * r + 1][3 * c + 2] = type == 1 or type == 4 or type == 6;
        }
    }
    
    return follow(ngrid, 1, 1);
}