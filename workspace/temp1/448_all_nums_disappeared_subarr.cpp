/* Nathan Zhu Tuesday Stockton, 7:05 am June 23nd, 2020.  I was pretty sad yesterday cuz I realized I might not go back to UM again. :(
*  Leetcode 448 | easy | not easy
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

using namespace std;


vector<int> findDisappearedNumbers(vector<int>& nums) {
    int N(nums.size());
    vector<int> ret;
    if(nums.empty()) return ret;
    bool n_exists = false;
    
    for(int i = 0; i < N; ++i){
        if(abs(nums[i]) == N) n_exists = true;
        else if(nums[abs(nums[i])] > 0) nums[abs(nums[i])] *= -1;
    }
    
    for(int i = 1; i < N; ++i)
        if(nums[i] > 0) ret.push_back(i);
    
    if(!n_exists) ret.push_back(N);
    return ret;
}