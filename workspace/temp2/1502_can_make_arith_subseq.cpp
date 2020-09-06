/* Nathan Zhu  Saturday July 11th, 2020 Stockton, CA, Weekly contest
*  Leetcode 1502 | easy | medium for O(N)?
*  Category: misc tricks
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
#include <climits>

using namespace std;



bool canMakeArithmeticProgression(vector<int>& arr) {
    int small(INT_MAX), sec_small(INT_MAX);
    unordered_map<int, int> counts;
    int N(arr.size());
    
    for(auto num : arr){
        if(num <= small){
            sec_small = small;
            small = num;
        }
        else if(num < sec_small){
            sec_small = num;
        }
        counts[num]++;
    }
    
    int delta = sec_small - small;  // 2+ elements in arr, so exists both
    int curr = small;
    for(int i = 0; i < N; ++i){
        if(counts.count(curr)) counts[curr]--;
        if(counts.count(curr) && counts[curr] == 0) counts.erase(curr);
        curr += delta;
    }
    
    return counts.empty();
}