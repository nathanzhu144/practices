/**
 * Nathan Zhu July 8th, 2021 6:12 pm.
 * Leetcode 813 | medium | medium
 * Category: DP
 * 
 * At alpine climbing gym, stockton, CA.  Got back from Utah this Monday.
*/

#include <vector>
#include <unordered_map>
#include <limits>
#include <string>

using namespace std;


// Space complexity O(K * N)
// Time complexity O(K * N ^ 2)
// Got it in first submit!

double helper(vector<int>& nums, int curr, int k, unordered_map<string, double>& table){
    int N = nums.size();
    string key = to_string(curr) + ":" + to_string(k);
    if(table.count(key)) return table[key];
    
    if(k < 0) return -numeric_limits<double>::infinity();
    if(curr == N) return 0;
    
    double ret = -numeric_limits<double>::infinity();
    int tot = 0;
    // curr is inclusive start index, end_i is inclusive end index of segment
    for(int end_i = curr; end_i < N; ++end_i){
        tot += nums[end_i];
        ret = max(ret, helper(nums, end_i + 1, k - 1, table) + (tot * 1.0) / (end_i - curr + 1));
    }
    
    table[key] = ret;
    return ret;
}
double largestSumOfAverages(vector<int>& nums, int k) {
    unordered_map<string, double> table;
    return helper(nums, 0, k, table);
}