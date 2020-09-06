
/* Nathan Zhu Wednesday July 21st, 2020 7:30 am Stockton, CA.  Talked to Jaewon yesterday.
*  Leetcode 1335 | hard | hard
*  Category: 2d DP
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



int MAXIMUM = 300 * 1000 + 1;

// d is number of days left
// pos is position in array
// jobs is passed in job difficulty array
// dp[pos][d] tracks subproblem at position pos & days d.
// max_subarr is 2d array w precalculated maximum of each subarray.
int helper(int pos, int d, vector<int>& jobs, vector<vector<int>>& dp){
    int N(jobs.size());
    if(d < 0) return MAXIMUM;               // can't use more than d days
    if(pos == N){
        if(d == 0) return 0;                // used up all days, 0 difficulty for no jobs left on no days
        else return MAXIMUM;                // did not use up all days
    }
    if(dp[pos][d] != -1) return dp[pos][d]; // seen this subproblem before, put this after negative checks

    
    int ret = MAXIMUM;
    int max_so_far = numeric_limits<int>::min();
    for(int i = pos; i < N; ++i){
        max_so_far = max(max_so_far, jobs[i]);
        ret = min(ret, max_so_far + helper(i + 1, d - 1, jobs, dp));
    }
    
    dp[pos][d] = ret;
    return ret;
}


int minDifficulty(vector<int>& jobs, int d) {
    int N(jobs.size());
    
    if(d > N) return -1;   // impossible
    
    vector<vector<int>> dp(N + 1, vector<int>(d + 1, -1));
    
    return helper(0, d, jobs, dp);
}