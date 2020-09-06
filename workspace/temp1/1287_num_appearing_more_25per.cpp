/* Nathan Zhu June 8th, 2020  
*  Leetcode 1287 | easy | medium
*  Category: binary search
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


// [1,2,2,6,6,6,6,7,10]
//  0 1 2 3 4 5 6 7 8

int findSpecialInteger(vector<int>& a) {
    int N(a.size());
    vector<int> arr = {a[N / 4], a[N / 2], a[3 * N / 4]};
    for(auto num : arr){
        auto left = lower_bound(begin(a), end(a), num);
        auto right = upper_bound(begin(a), end(a), num);
        if ((std::distance(left, right) * 4) > N) return num;
    }
    return -1;
}