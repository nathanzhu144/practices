/* Nathan Zhu Tuesday Stockton, CA. 12:08 am June 23rd, 2020.  I watched a william lin video of him doing 150 questions in 12 hours lol.  OK my dude.
*  Leetcode 491 | medium | medium
*  Category:  backtracking
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


void helper(vector<vector<int>>& ret, vector<int>& nums, int pos, vector<int>& currpath){
    int N(nums.size());
    if(currpath.size() > 1) ret.push_back(currpath);
    unordered_set<int> visited;
    for(int i = pos; i < N; ++i){
        // This is really smart.  Note this allows consecutive numbers, in diff recursive frames.
        if((!currpath.size() || currpath.back() <= nums[i]) && !visited.count(nums[i])){
            currpath.push_back(nums[i]);
            helper(ret, nums, i + 1, currpath);
            currpath.pop_back();
            visited.insert(nums[i]);
        }
        
    }
}
    
vector<vector<int>> findSubsequences(vector<int>& nums) {
    vector<int> currpath;
    vector<vector<int>> ret;
    helper(ret, nums, 0, currpath);
    return ret;
}