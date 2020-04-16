/*  Nathan Zhu Monday, April 13th, 2020 11:26 am, Stockton, CA
*   Leetcode 1349 | hard | kind hard
*   Category: DP / bits
*   This is a very special DP problem where it is possible to use bit operations to significantly speed up some of the brute
*   force comparisons.
*
*   We memoize on (row, student orientation)
*   This is calculated bottom-up without backtracking but can be done with backtracking.
*   
*   Naive backtracking soln is written below.
*/

#include <vector>
#include <algorithm>
using namespace std;
// Note: masks[i - 1] & j == j 
// & has lower prec than ==, so this is always true. Be carefu.

// This is a more optimized set bit algorithm.
// Runs O(number of set bits)
// Note: can use __builtin_popcount(n) to get number of bits in a set number
//       this is a highly optimized gcc routine
int set_bits(int n){
    int ret = 0;
    for(; n ; ++ret) n = n & (n - 1);
    return ret;
}

int maxStudents(vector<vector<char>>& seats) {
    vector<int> masks;   // This is a vector that holds all the bitmasks for each seat row
                            // Bitmask has a 1 if the seat is not broken.
    if (!seats.size()) return 0;
    
    int R = seats.size(), C = seats[0].size();
    for(int r = 0; r < R; ++r){
        int curr = 0;
        for(int c = 0; c < C; ++c){
            curr = 2 * curr + int(seats[r][c] == '.');
        }
        masks.push_back(curr);
    }
    
    vector<vector<int>> dp(R + 1, vector<int>(1 << C, -1));
    dp[0][0] = 0;
    // iterate thru all rows
    for(int i = 1; i <= R; ++i){  
        // j in binary represents all possible seating arrangements for the i-th row
        for(int j = 0; j < (1 << C); ++j){
            
            // (masks[i - 1] & j) == j  checks to see if j is a subset of masks[i - 1]
            // !(j & (j >> 1))          check to see if j has no consecutive ones
            if((masks[i - 1] & j) == j and !(j & (j >> 1))){
                // iterate thru all previous masks
                for(int k = 0; k < (1 << C); ++k){
                    
                    // !(k >> (1 & j)) checks no student at top left
                    // !((k << 1) & j) checks no student at top right
                    // dp[i - 1][k] != -1 checks to see if k is a valid configuration on last row
                    if(!((k >> 1) & j) and !((k << 1) & j) and dp[i - 1][k] != -1){
                        // set bits calculates number of students we can add in this row.
                        dp[i][j] = max(dp[i][j], dp[i - 1][k] + set_bits(j)); 
                    }
                }
            }
        }
    }
    
    return *max_element(dp[R].begin(), dp[R].end());
}

// Naive backtracking soln
// def maxStudents(grid):
//     """
//     :type seats: List[List[str]]
//     :rtype: int
//     """
    
//     if not grid or not grid[0]: return 0
//     ret = [0]
    
//     def get_next(r, c):
//         R, C = len(grid), len(grid[0])
//         if c == C - 1: return (r + 1, 0)
//         else: return (r, c + 1)
    
//     def helper(r, c, curr):
//         R, C = len(grid), len(grid[0])
//         if r == R: 
//             ret[0] = max(curr, ret[0])
//             return 
//         nextr, nextc = get_next(r, c)
        
//         # Seat is broken, cannot fit a student.
//         if grid[r][c] == "#": 
//             helper(nextr, nextc, curr)
//             return
            
//         for dr, dc in [(0, -1), (0, 1), (-1, -1), (-1, 1)]:
//             newr, newc = dr + r, dc + c
//             if not (0 <= newr < R and 0 <= newc < C): continue
//             if grid[newr][newc] == "s":
//                 helper(nextr, nextc, curr)
//                 return
            
//         grid[r][c] = "s"
//         helper(nextr, nextc, curr + 1)
//         grid[r][c] = '.'
//         helper(nextr, nextc, curr)
        
        
//     helper(0, 0, 0)
//     return ret[0]