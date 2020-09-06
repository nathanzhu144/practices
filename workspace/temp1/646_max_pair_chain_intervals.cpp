/* Nathan Zhu Monday Stockton, CA. 10:18 pm June 22nd, 2020.  I watched a william lin video of him doing 150 questions in 12 hours lol.  OK my dude.
*  Leetcode 646 | medium | medium
*  Category: DP / Greedy
*  This is the same problem as finding the most number of meetings you go to given intervals.
*  I do it here the greedy way with sorting, but also can do it with N^2 with DP.
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
    if(N == 0) return 0;
    sort(begin(pairs), end(pairs), [](auto& p1, auto& p2){ return p1[1] < p2[1]; });
    int last_end = pairs[0][0] - 1;
    
    for(int i = 0; i < N; ++i){
        if(pairs[i][0] > last_end){
            ret++;
            last_end = pairs[i][1];
        }
    }
    
    return ret;
}


