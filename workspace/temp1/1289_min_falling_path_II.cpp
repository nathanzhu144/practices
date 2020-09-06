/* Nathan Zhu June 8th, 2020  
*  Leetcode 1289 | hard | hard
*  Category: DP
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
#include <climits>
#include <cmath>
#include <limits>
#include <iostream>

using namespace std;


int minFallingPathSum(vector<vector<int>>& arr) {
    int R(arr.size()), C(arr[0].size());
    vector<vector<int>> dp(R, vector<int>(C, INT_MAX));
    for(int c = 0; c < C; ++c) dp[0][c] = arr[0][c];
    
    for(int r = 1; r < R; ++r){
        for(int c = 0; c < C; ++c){
            for(int prevc = 0; prevc < C; ++prevc){
                if(c == prevc) continue;
                dp[r][c] = min(dp[r][c], arr[r][c] + dp[r - 1][prevc]);
            }
        }
    }
    
    int ret = dp[R - 1][0];
    for(int c = 0; c < C; ++c) ret = min(ret, dp[R - 1][c]);
    return ret;
}