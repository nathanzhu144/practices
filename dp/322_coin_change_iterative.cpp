/* Nathan Zhi May 14th, 2020, Stockton, CA.  Stanford guy told me to do more LC today, good stuff!
*  Leetcode 322 | medium | EZ
*  Category: Basic dp
*
*  Note, we cannot add to numeric limits max unlike python's float inf.
*/

#include <vector>
#include <limits>

using namespace std;

int coinChange(vector<int>& coins, int N) {
    vector<int> dp(N + 1, numeric_limits<int>::max());
    dp[0] = 0;   // 0 cent -> 0 coins.
    
    for(int i = 1; i <= N; ++i){
        for(auto coin : coins){
            if(i - coin >= 0 and dp[i - coin] < numeric_limits<int>::max())
                dp[i] = min(dp[i - coin] + 1, dp[i]);
        }
    }
    
    return dp[N] == numeric_limits<int>::max() ? -1 : dp[N]; 
}