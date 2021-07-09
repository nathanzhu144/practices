/* Nathan Zhu June 8th, 2021. 5:35 pm, got back from Utah trip on Monday, ran a 10:07 pace  for a 5k two days ago
*  Leetcode 1658 | medium | interesting
*  Category: Prefix sum
*/

#include <vector>

using namespace std;

int minOperations(vector<int>& nums, int x) {
    //Thoughts:
    // Backtracking is 2^N.  Better idea is to see this as finding the length of the
    // longest continuous subarray w length sum(nums) - x, and then returning len(nums) - x.
    //
    // Doable w sliding window, but also presum with hash table.  This is second approach.
    // O(N) time, O(N) space.
    //
    // Edge case: 
    // Need to use up all elements to reduce x to 0.
    //
    //ret tracks length longest continuous subarray w sum sum(nums) - x
    int target = accumulate(begin(nums), end(nums), 0) - x, curr = 0, ret = -1, N = nums.size();
    
    if(target == 0) return N;
    
    unordered_map<int, int> table; //represents presums seen @ prev positions
    
    table[0] = -1;
    
    for(int i = 0; i < N; ++i){
        curr += nums[i];
        
        if(table.count(curr - target)){
            ret = max(ret, i - table[curr - target]);
        }
        
        table[curr] = i;
    }
    
    return ret != -1 ? N - ret : -1; 
}