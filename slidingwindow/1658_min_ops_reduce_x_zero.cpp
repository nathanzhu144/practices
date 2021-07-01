/* Nathan Zhu July 1st, 2021
*  Leetcode 1658 | medium | medium
*  Category: Sliding window
*  With hershal & emil in salt lake city.  Yesterday, on third visit to the front climbing
*  gym in SLC, I sended one of the top ropes w the blue holds.  We went to inn and out last 
*  night and Purgatory.  
*/

#include <iostream>
#include <vector>


using namespace std;

// Sliding window approach.
// Insight: 
// Naive approach, like backtracking, is exhaustively slow, O(2^N)
// There is an O(N) approach.  What's the longest continuous sequence
// with a sum of sum(nums) - x.  Easy sliding window problem, then.

int minOperations(vector<int>& nums, int x) {
    int l = 0, r = 0, ret = nums.size() + 1, curr = 0, N = nums.size();
    int target = std::accumulate(begin(nums), end(nums), 0) - x;
    
    if(target < 0) return -1;
    
    
    while(r < N){
        while(r < N && curr < target){
            curr += nums[r];
            r++;
        }
        
        while(l <= r && l < N && curr >= target){
            if(curr == target){
                ret = min(ret, N - (r - l));
            }
            curr -= nums[l];
            l++;
        }
    }
    
    return (ret == N + 1) ? -1 : ret;
}