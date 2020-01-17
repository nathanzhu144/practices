/* Nathan Zhu December 24th, 2019 Did this on paper way to sugar bowl ski resort on December 21s, 2019
*  Leetcode 883 | easy | easy yo
*  Category: misc-tricks
*  
*  Having a basic understanding of linear algebra makes this question trivial.

    On a N * N grid, we place some 1 * 1 * 1 cubes that are axis-aligned with the x, y, and z axes.
    Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).
    Now we view the projection of these cubes onto the xy, yz, and zx planes.
    A projection is like a shadow, that maps our 3 dimensional figure to a 2 dimensional plane. 
    Here, we are viewing the "shadow" when looking at the cubes from the top, the front, and the side.
    Return the total area of all three projections.
*/


#include <vector>
#include <algorithm>
#include <numeric> // accumulate

using namespace std;

int projectionArea(vector<vector<int>>& grid) {
    int R = grid.size();
    int C = grid[0].size();
    
    // rows represents maximum height of blocks on that row
    // cols represents maximum height of blocks on that col
    vector<int> rows(R);
    vector<int> cols(C);
    
    int ret = 0;
    for(int r = 0; r < R; ++r){
        for(int c = 0; c < C; ++c){
            if(grid[r][c] == 0) continue;
            ret++;
            
            rows[r] = max(rows[r], grid[r][c]);
            cols[c] = max(cols[c], grid[r][c]);
        }
    }
    
    ret += accumulate(rows.begin(), rows.end(), 0);
    ret += accumulate(cols.begin(), cols.end(), 0);
    
    return ret;
}