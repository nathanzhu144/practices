/** Nathan Zhu Saturday September 21st, 2019, 9:10 am Week after career fair
 * 
 * You have a number of envelopes with widths and heights given as a pair of integers
 * (w, h). One envelope can fit into another if and only if both the width and height 
 *  of one envelope is greater than the width and height of the other envelope.
 * 
 * This is a hidden longest increasing subsequence problems.  
 * We sort, it by INCREASING width, and DECREASING Height.
 * 
*/

#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;


class Comp{
    public:
    bool operator()(vector<int>& env1, vector<int>& env2){
        if(env1[0] == env2[0]){ return env1[1] > env2[1]; }
        return env1[0] < env2[0];
    }
    
};


// Returns tru if we can fit env1 in env2
bool can_fit(vector<int>& env1, vector<int>& env2){
    return env1[0] < env2[0] && env1[1] < env2[1];
}

// Standard algorithm for finding LiS in N^2 time.
int LIS(vector<vector<int>>& envelopes){
    vector<int> dp(envelopes.size(), 1);
    int ret = 1;
    
    for(int i = envelopes.size() - 1; i >= 0; i--){
        for(int j = i + 1; j < envelopes.size(); ++j){
            if(can_fit(envelopes[i], envelopes[j])){
                dp[i] = max(dp[j] + 1, dp[i]);
                ret = max(ret, dp[i]);
            }
        }
    }
    
    return ret;
    
}
int maxEnvelopes(vector<vector<int>>& envelopes) {
    if(envelopes.empty()) return 0;
    std::sort(envelopes.begin(), envelopes.end(), Comp());
    
    
    return LIS(envelopes);
}



int main(){
    vector<vector<int>> vec = {{46, 89}, {50, 53}, {52, 68}, {72, 45}, {77, 81}};
    cout << maxEnvelopes(vec);
}