/* Nathan Zhu Stockton, CA, June 1st, 2020. 8:18 ams Tomorrow is the first day I start at Amex last year! :O
*  Leetcode 1365 | easy | easy
*  Category: bucket sort
*
*  Ask about range when sorting numbers.
*/

#include <vector>

using namespace std;

vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
    vector<int> buckets(101);
    vector<int> ret(nums.size());
    for(auto num : nums) buckets[num] += 1;
    for(int i = 1; i <= 100; ++i) buckets[i] += buckets[i - 1];
    for(int i = 0; i < nums.size(); ++i){
        ret[i] = (nums[i] == 0) ? 0 : buckets[nums[i] - 1];
    }
    return ret;
}