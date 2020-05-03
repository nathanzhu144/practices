/* Nathan Zhu April 18th, 2020 Stockton, CA during biweekly leetcode contest
*  Leetcode 1413 | easy | easy
*  Category: Fizzbuzz
*/

#include <vector>

using namespace std;

int minStartValue(vector<int>& nums) {
    int N = nums.size();
    vector<int> prefix(nums.begin(), nums.end());
    
    int ret = nums[0];
    for(int i = 1; i < N; ++i){
        prefix[i] += prefix[i - 1];
        ret = min(prefix[i], ret);
    }
    
    if (ret >= 0) return 1;
    return -ret + 1;
}