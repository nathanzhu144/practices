/* Nathan Zhu May 7th, 2020. Starting Salesforce in a week or so!
*  Leetcode 78 | medium | not bad
*  Category: Backtracking / recursion
*/
#include <vector>

using namespace std;


vector<vector<int>> helper(vector<int> nums){
    if(nums.size() == 0) return {{}};
    
    vector<vector<int>> ret;
    for(auto& vec: helper(vector<int>(next(nums.begin()), nums.end()))){
        ret.push_back(vec);
        vec.push_back(nums[0]);
        ret.push_back(vec);
    }
    return ret;
}
vector<vector<int>> subsets(vector<int>& nums) {
    return helper(nums);
}