/* Nathan Zhu Monday Stockton, CA. 10:18 pm June 22nd, 2020.  Just realized might not be going back to UM for a long time today.  :(  Got an email from Mark Sch about 
*                                                             semester being online.
*  Leetcode 646 | medium | medium
*  Category: DP / Greedy
*  Doing it N^2 with DP here.
*  Can maybe get it to NLogN with binary search?  I think the string sequence increases monotonically with
*  the last chain amount.  We want to find the largest number for which we can tack a chain on.
*  Didn't try it but think it is possibles
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


int findLongestChain(vector<vector<int>>& pairs) {
    int N(pairs.size()), ret(0);
    unordered_map<int, int> table;   // ending val -> longest chain ending at this val
    sort(begin(pairs), end(pairs), [](auto& a, auto&b){ return a[1] < b[1]; });
    
    for(int i = 0; i < N; ++i){
        int curr = 1;  // need this to be 1, worst case we can make a len 1 chain
        for(auto [last_end, v] : table){
            if(last_end < pairs[i][0]) curr = max(curr, 1 + table[last_end]);
        }
        table[pairs[i][1]] = max(curr, table[pairs[i][1]]);
        ret = max(curr, ret);
    }
    
    return ret;
}