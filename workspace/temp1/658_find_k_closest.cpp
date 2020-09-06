/* Nathan Zhu Friday Stockton, CA. 10:29 pm June 19th, 2020.  Day off on Friday today. :)
*  Leetcode 658 | medium | medium
*  Category: binary search
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

// right is greater or eq to k.
// so, left should be less or eq to k.
// Note: can combine to 3 cases, but 5 cases is more clear.
//
// Also, we can get min(logN + K) if we just keep track of where left & right are
// and then return that window at the end.
vector<int> findClosestElements(vector<int>& arr, int k, int x) {
    vector<int> ret;
    auto right = lower_bound(begin(arr), end(arr), x);
    auto left = (right == begin(arr)) ? end(arr) : prev(right);
    while(k--){
        if(left == end(arr)){
            ret.push_back(*right);
            right = next(right);
        }
        else if(right == end(arr)){
            ret.push_back(*left);
            left = prev(left);
        }
        else if(abs(x - *right) < abs(x - *left)){
            ret.push_back(*right);
            right = next(right);
        }
        else if(abs(x - *right) == abs(x - *left)){
            ret.push_back(*left);
            left = (left == begin(arr)) ? end(arr) : prev(left);
        }
        else{
            ret.push_back(*left);
            left = (left == begin(arr)) ? end(arr) : prev(left);
        }
    }
    
    sort(begin(ret), end(ret));
    return ret;
}