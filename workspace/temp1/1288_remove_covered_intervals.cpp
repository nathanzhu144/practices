/* Nathan Zhu June 8th, 2020  
*  Leetcode 1288 | medium | medium
*  Category: intervals, greedy
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
#include <climits>
#include <cmath>
#include <limits>
#include <iostream>

using namespace std;


int removeCoveredIntervals(vector<vector<int>>& intervals) {
    // Normally, we can use the default comparator for 2d vectors, which will sort
    // from smallest to biggest. Tiebreak with 2nd element.
    // However, we want this kind of sorting [1,4], [1,2], [5, 6] as
    // [1,4], [1,2], [5,6].  This is because we want the larger right borders first.
    
    auto func = [](vector<int>& a, vector<int>& b){
        if(a[0] == b[0]) return a[1] > b[1];  // largest right borders
        else return a[0] < b[0];
    };
    
    sort(begin(intervals), end(intervals), func);
    vector<pair<int, int>> ret;
    for(auto& i: intervals){
        auto s(i[0]), e(i[1]);
        if(!ret.size() || ret.back().second < e) ret.emplace_back(s, e); 
    }
    return ret.size();
}