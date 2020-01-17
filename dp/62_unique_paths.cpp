/**
 * Nathan Zhu Friday Jan 10th, 2019
 * Leetcode 62 | medium | EZ
 * Category: DP
 * 
 * This one is basic.
*/

using namespace std;
#include <vector>

int uniquePaths(int m, int n) {
    vector<vector<int>> grid(m, vector<int>(n, 0));
    
    int R = m;
    int C = n;
    
    for(int r = 0; r < R; ++r) grid[r][0] = 1;
    for(int c = 0; c < C; ++c) grid[0][c] = 1;
    
    for(int r = 1; r < R; ++r){
        for(int c = 1; c < C; ++c){
            grid[r][c] = grid[r - 1][c] + grid[r][c - 1];
        }
    }
    return grid[R - 1][C - 1];
}


// Python Top-down version
// def uniquePaths(m, n):
//     """
//     :type m: int
//     :type n: int
//     :rtype: int
//     """
//     def helper(m, n, mem):
//         key = (m, n)
        
//         if mem.has_key(key):
//             return mem[key]
        
//         if m == 0 or n == 0:
//             mem[key] = 1
            
//         else:
//             mem[key] = helper(m - 1, n, mem) + helper(m, n - 1, mem)
            
//         return mem[key]
    
//     return helper(m - 1, n - 1, {})