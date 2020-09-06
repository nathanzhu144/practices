/* Nathan Zhu Friday Stockton, CA. 10:41 pm June 19th, 2020.  Day off on Friday today. :)
*  Leetcode 993 | easy | medium
*  Category: BFS
*/


#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <set>
#include <string>
#include <queue>
#include <deque>
#include <utility>
#include <algorithm>
#include <cmath>
#include <limits>
#include <iostream>

using namespace std;


// Originally, I was trying to put a placeholder value in the beginning.
// However, this doesn't work too well, I think.
// The placeholder value is for PERFORMING INTERVALS THAT START FROM INDEX 0.
// Ex. 6, 9, 9  9
//     -1 0  1  2 (should be 4, but value at 0 cannot be all possible values -1)
//
// An easier way is to say that if curr > 0, the whole prefix is well-performing.
// Then ret = max(ret, i + 1)
int longestWPI(vector<int>& hours) {
    unordered_map<int, int> first_pt;
    
    int ret(0), N(hours.size()), curr(0);
    for(int i = 0; i < N; ++i){
        curr += (hours[i] > 8) ? 1 : -1;
        if(curr > 0) ret = max(ret, i + 1);
        if(first_pt.count(curr - 1)) ret = max(ret, i - first_pt[curr - 1]);
        if(!first_pt.count(curr)) first_pt[curr] = i;
    }
    return ret;
}