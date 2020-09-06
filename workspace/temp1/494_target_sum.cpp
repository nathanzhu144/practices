/* Nathan Zhu Monday Stockton, CA. 1:25 am June 22nd, 2020.  I watched a william lin video of him doing 150 questions in 12 hours lol.  OK my dude.
*  Leetcode 494 | medium | easy if no dp
*  Category: DP, recursion
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

// curr == currsu
// i == index in nums
// target == S or targetnum
int helper(vector<int>& nums, int curr, int i, int target){
    int N(nums.size());
    if(i == N) return (curr == target) ? 1 : 0;
    return helper(nums, curr + nums[i], i + 1, target) + helper(nums, curr - nums[i], i + 1, target);
}
int findTargetSumWays(vector<int>& nums, int S) {
    return helper(nums, 0, 0, S);
}