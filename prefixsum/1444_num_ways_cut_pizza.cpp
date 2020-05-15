/* Nathan Zhu April 14, 2020.  Starting at Salesforce in 4 days!
*  Leetcode 1444 | hard | yes hard
*  Category: 3d DP, prefix sum
*
*  I absolutely had no idea how to do this during the contest.  It actually was easier than expected.
*  
*/

#include <vector>
#include <string>
using namespace std;

const int MOD = 1e9 + 7;

int dfs(vector<vector<int>>& apples, int r, int c, int k, vector<vector<vector<int>>>& dp){
    if(apples[r][c] == 0) return 0;               // Down slice no apple, return false
    if(dp[r][c][k] != -1) return dp[r][c][k];
    if(k == 0) return 1;
    int ret = 0;
    
    // Here we cut horizontally.
    // apples[dr + r][dc] != apples[r][c] ensures up slice has an apple
    // Note: apples.size - 1 is cuz I make apples 1 row and 1 col bigger than it should be for easier prefix sum calc
    for(int dr = 1; dr + r < apples.size() - 1; ++dr){
        if(apples[dr + r][c] < apples[r][c]){
            ret += dfs(apples, dr + r, c, k - 1, dp);
            ret %= MOD;
        }
    }
    
    // Here we cut vetically.
    for(int dc = 1; dc + c < apples[0].size() - 1; ++dc){
        if(apples[r][dc + c] < apples[r][c]){
            ret += dfs(apples, r, c + dc, k - 1, dp);
            ret %= MOD;
        }
    }
    
    dp[r][c][k] = ret;
    return ret;
}

int ways(vector<string>& pizza, int k) {
    int R(pizza.size()), C(pizza[0].size());
    
    vector<vector<int>> apples(R + 1, vector<int>(C + 1, 0));
    vector<vector<vector<int>>> dp(R, vector<vector<int>>(C, vector<int>(k + 1, -1))); 
    
    // Prefix sum calc
    for(int r = R - 1; r >= 0; --r){
        for(int c = C - 1; c >= 0; --c){
            if(pizza[r][c] == 'A') apples[r][c] = 1;
            apples[r][c] += apples[r + 1][c] + apples[r][c + 1] - apples[r + 1][c + 1];
        }
    }
    
    return dfs(apples, 0, 0, k - 1, dp);          // pass in k - 1 because we want to do k - 1 cuts for k slices.
}