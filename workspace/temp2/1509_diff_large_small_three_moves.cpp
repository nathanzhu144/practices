/* Nathan Zhu  Saturday July 11th, 2020 Stockton, CA, Weekly contest
*  Leetcode 1509 | medium | medium
*  Category: misc tricks
*/

#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <set>
#include <stack>
#include <map>
#include <string>
#include <queue>
#include <deque>
#include <utility>
#include <algorithm>
#include <cmath>
#include <limits>
#include <iostream>

using namespace std;


long helper(map<long, long>& counts, int low, int high){
    if(low > 0){
        if(counts.size()){
            long val = counts.begin()->first;
            counts[val]--;
            if(counts[val] == 0) counts.erase(val);
            long ret = helper(counts, low - 1, high);
            counts[val]++;
            return ret;
        }
        return helper(counts, low - 1, high);
    }
    else if(high > 0){
        if(counts.size()){
            long val = counts.rbegin()->first;
            counts[val]--;
            if(counts[val] == 0) counts.erase(val);
            long ret = helper(counts, low, high - 1);
            counts[val]++;
            return ret;
        }
        return helper(counts, low, high - 1);
    }
    else return (counts.size()) ? counts.rbegin()->first - counts.begin()->first : 0;
}

int minDifference(vector<int>& nums) {
    map<long, long> counts;
    
    for(auto num : nums){
        counts[num]++;
    }
    
    long first = helper(counts, 0, 3);
    long sec = helper(counts, 1, 2);
    long th = helper(counts, 2, 1);
    long fo = helper(counts, 3, 0);
    
    return min(min(first, sec), min(th, fo));
}