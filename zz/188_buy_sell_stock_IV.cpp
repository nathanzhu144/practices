#include <iostream>
#include <vector>

using namespace std;

int maxProfit(int l, vector<int> prices) {
    if(l == 0) return 0;
    if(prices.empty()) return 0;
    
    vector<vector<int> > dp(l + 1, vector<int>(prices.size(), 0));

    for(int k = 1; k < l + 1; ++k){
        for(int i = 1; i < prices.size(); ++i){
            for(int j = 0; j < i; ++j){
                dp[k][i] = dp[k][i - 1];
                dp[k][i] = max(dp[k][i], dp[k - 1][j] + prices[i] - prices[j]);
            }
        }
    }
    
    return dp[l][prices.size() - 1];
}

int main(){
    cout << maxProfit(1, {6, 1, 3, 2, 4, 7});
    return 0;
}