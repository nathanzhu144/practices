/** Nathan Zhu April 16th, 2020. Stockton, CA during COVID-19
 *  Leetcode 698 | medium | medium
 *  Category: DFS
*/

#include <vector>
using namespace std;
bool helper(int i, int curr, int num_made, int target_sum, int target_sums_made, vector<int>& nums, vector<int>& table){
    if (curr == target_sum){
        if(num_made + 1 == target_sums_made) return true;
        else return helper(0, 0, num_made + 1, target_sum, target_sums_made, nums, table);
    }
    if (i >= nums.size()) return false;
    
    bool ret = false;
    int curr_sum = curr;
    for(int start = i; i < nums.size(); ++i){
        if(!table[i]) continue;
        if(curr_sum + nums[i] <= target_sum){
            table[i] = 0;
            if (helper(i + 1, curr + nums[i], num_made, target_sum, target_sums_made, nums, table)) return true;
            table[i] = 1;             
        }
    }
    return ret;
    
}

bool canPartitionKSubsets(vector<int>& nums, int k) {
    int tot = 0;
    for(auto num : nums) tot += num;
    
    if(tot % k != 0) return false;
    
    int target_sum = tot / k;
    vector<int> table(nums.size(), 1);
    return helper(0, 0, 0, target_sum, k, nums, table);
}