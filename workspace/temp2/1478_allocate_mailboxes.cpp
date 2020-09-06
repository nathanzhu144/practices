/* Nathan Zhu Tuesday July 14th, 2020  Stockton, CA. TACO TUESDAY
*  Deploying golang projects to Heroku is really fun.  :P
*  Leetcode 1478 | hard | hard
*  Category: DP
*
*  DAMN THIS SOLUTION IS SMART.
*  I got as far as figuring out the best way to minimize distance with 1 mailbox was the median, lol.
*  What about more than one mailbox?
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

int BIGGEST_NUM = 1000000;  // used in place of INT_MAX, as INT_MAX + 1 gives overflow in C++

// dp maps (curr, k) -> previous values
// distances is cost when a mailbox services from [i][j] inclusive of both sides
// curr is position in array
// k is the number of mailboxes left
int helper(vector<int>& houses, int curr, int k, vector<vector<int>>& distances, vector<vector<int>>& dp){
    if(k < 0) return BIGGEST_NUM;
    if(curr == houses.size()) return (k == 0) ? 0 : BIGGEST_NUM;  // only return 0 if we used all mailboxes
    if(dp[curr][k] != -1) return dp[curr][k];
    
    int cost = BIGGEST_NUM;
    for(int i = curr; i < houses.size(); ++i){
        cost = min(cost, distances[curr][i] + helper(houses, i + 1, k - 1, distances, dp));
    }
    
    dp[curr][k] = cost;
    return cost;
}

// Why does calculating as abs(houses[(j + i) / 2]) work?
// What if there are an even number of houses in this range?
// Ex. 1 2 4 8
// idx 0 1 2 3
//
// We are fixing the mailbox at position 2, house[(0 + 3) / 2] == house[1]
// instead of at position 3 in between 2 and 4.  This works because even though
// houses 4 & 8 are 1 farther away from 2 than they would be 3, 1 & 2 are each 1 closer.
// So, the conclusion is that whatever value we place the mailbox at between 2 & 4, 
// we could get a minimum distance.
int minDistance(vector<int>& houses, int k) {
    sort(begin(houses), end(houses));
    int MAX_H = 100;
    
    vector<vector<int>> distances(MAX_H, vector<int>(MAX_H, 0));
    vector<vector<int>> dp(MAX_H, vector<int>(MAX_H, -1));
    int N = houses.size();

    // Precalculating all mailbox placements and the costs for the houses they can serve
    for(int i = 0; i < N; ++i){
        for(int j = i; j < N; ++j){
            for(int m = i; m <= j; ++m){
                distances[i][j] += abs(houses[(j + i) / 2] - houses[m]);
            }
        }
    }
    
    return helper(houses, 0, k, distances, dp);
}