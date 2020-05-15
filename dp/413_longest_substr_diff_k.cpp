/* Nathan Zhu May 9th, 2020. I did the sliding window-ish approach yesterday, this is the DP way.
*  Leetcode 413 | medium | medium
*  Category: DP
*/

#include <vector>

using namespace std;


int numberOfArithmeticSlices(vector<int>& A) {
    int N = A.size();
    if(N < 3) return 0;
    vector<int> dp(N, 0);
    int ret = 0;
    
    if(A[1] - A[0] == A[2] - A[1]) dp[2] = 1;
    ret += dp[2];
    
    for(int i = 3; i < N; ++i){
        if(A[i] - A[i - 1] == A[i - 1] - A[i - 2]){
            dp[i] = dp[i - 1] + 1;
        }
        ret += dp[i];
    }
    return ret;
}