/* Nathan Zhu Tuesday August 18th 2020 Chicago, IL, Just got to chicago two days ago.
*  Leetcode 1347 | medium | easy
*  Category: misc trick
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


vector<vector<int>> threeSum(vector<int>& arr) {
    int N(arr.size());
    sort(begin(arr), end(arr));
    vector<vector<int>> ret;
    
    for(int i = 0; i < N - 2; ++i){
        while(i > 0 && i < N && arr[i] == arr[i - 1]) ++i;
        int left(i + 1), right(N - 1);
        
        while(left < right){
            int tot(arr[i] + arr[left] + arr[right]);
            
            if(tot == 0){
                ret.push_back({arr[i], arr[left], arr[right]});
                while(left + 1 < N && arr[left] == arr[left + 1]) ++left;
                while(right - 1 >= 0 && arr[right] == arr[right - 1]) --right;
                ++left;
                --right;
            }
            else if(tot > 0) --right;
            else ++left;
        }
    }
    return ret;
}