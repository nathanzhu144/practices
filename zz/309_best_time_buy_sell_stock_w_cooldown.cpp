/**
 * Nathan Zhu Monday Sept 23rd, 2019 8:43 am before EECS 484 class.
 * Leetcode 309 | medium | hard
 * Category: Finite state machine / DP
 * 
 * This has been a wild journey, and I think I finally get this one now.
 * 
 */
#include <limits>
#include <bits/stdc++.h> 
#include <iostream>
#include <vector>

using namespace std;

int maxProfit(vector<int>& prices) {
    if(prices.empty()) return 0;
    vector<int> buy(prices.size(), 0);
    vector<int> sell(prices.size(), 0);
    vector<int> rest(prices.size(), 0); 
    
    sell[0] = INT_MIN;
    buy[0] = -prices[0];
    
    for(int i = 1; i < prices.size(); ++i){
        buy[i] = max(buy[i - 1], rest[i - 1] - prices[i]);
        sell[i] = buy[i - 1] + prices[i];
        rest[i] = max(rest[i - 1], sell[i - 1]);
    }
    
    return max(rest.back(), sell.back());
}