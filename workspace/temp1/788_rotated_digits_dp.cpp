


/* Nathan Zhu Tuesday, Stockton, CA. 6:51 pm, June 16th, 2020 Called Sophie from Amex today.
*  Leetcode 1219 | medium | EZ
*  Category: DP
*  If you're smart, you can re-use the fact that if you break a number up into the tens digit (and up), and the ones 
*  digit, and keep track of 3 statuses, you can actually build a recurrence relation
*/
#include <vector>
using namespace std;
int rotatedDigits(int N) {
    vector<int> dp(N + 1, 0);
    int ret = 0;
    // dp[i] = 0 invalid num
    // dp[i] = 1 valid num, but same num
    // dp[i] = 2 valid num, and num has changed
    
    for(int i = 0; i <= N; ++i){
        // base cases
        if(i < 10){
            if(i == 0 || i == 1 || i == 8) dp[i] = 1;
            else if(i == 2 || i == 5 || i == 6 || i == 9){
                dp[i] = 2;
                ret++;
            }
        }
        // Split into two pieces calculated before
        else{
            if(dp[i / 10] == 1 && dp[i % 10] == 1) dp[i] = 1;
            else if(dp[i / 10] >= 1 && dp[i % 10] >= 1){
                dp[i] = 2;
                ret++;
            }
        }
    }
    return ret;
}