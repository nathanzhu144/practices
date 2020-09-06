/* Nathan Zhu Thursday, June 4th, 2020. Stockton, CA, 8:05 pm, called Kareen today. 
*  Leetcode 1320 | hard | kind hard
*  Category: 3d DP.
*/

#include <cmath>
#include <string>

using namespace std;

int cost(int from, int to){
    if(from == 26) return 0;  // we "choose" finger position for first key, so 0 cost.
    return abs(from / 6 - to / 6) + abs(from % 6 - to % 6);
}

int helper(string& word, int dp[27][27][301], int left, int right, int pos){
    if(pos == word.size()) return 0;
    
    if(dp[left][right][pos] == -1){   // -1 means not calculated.
        int to = word[pos] - 'A';
        dp[left][right][pos] = min(cost(left, to) + helper(word, dp, to, right, pos + 1), 
                                    cost(right, to) + helper(word, dp, left, to, pos + 1));
    }
                                        
    return dp[left][right][pos];
}

int minimumDistance(string word) {
    // Dp table represents: 
    // [left finger pos][right finger pos][position in string]
    // Position 0 for left/right finger represent A
    // Position 26 for left/right finger represents finger not used yet (so we can make cost 0 for first keypress)
    int dp[27][27][301] = {};
    for(int i = 0; i < 27; ++i){
        for(int j = 0; j < 27; ++j){
            for(int k = 0; k < 301; ++k) dp[i][j][k] = -1;
        }
    }
    return helper(word, dp, 26, 26, 0);
}