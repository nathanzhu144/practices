/** Nathan Zhu Feb 1st, 2020.  Old memories.  Went to UM Winter career fair today.
 *  Leetcode 1 | easy | easy
 *  Category: Fizzbuzz
*/
#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;


vector<int> twoSum(vector<int>& nums, int target) {
    unordered_map<int, int> table;
    int N = nums.size();
    
    for(int i = 0; i < N; ++i){
        auto temp = table.find(target - nums[i]);
        if(temp != table.end()) return {temp->second, i};
        table[nums[i]] = i;
    }
    return {};
}