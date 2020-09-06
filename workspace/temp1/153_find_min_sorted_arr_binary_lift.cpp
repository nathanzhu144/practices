/*  Nathan Zhu June 14th, 2020 11:01 pm, got a binary lifting question on the contest today for the hard, didn't know what it was.
*   Leetcode 153 | medium | medium
*   Category: Binary lifting
*/

#include <vector>
#include <cmath>
using namespace std;

int findMin(vector<int>& nums) {
    int N(nums.size());
    int logn(log2(N)), curr(0);
    if(N == 1 || nums[0] < nums.back()) return nums[0];   // We return out of bounds otherwise for [1]  OR [1, 2]
    
    for(int i = logn; i >= 0; --i){
        if(curr + (1 << i) < N && nums[curr + (1 << i)] > nums[0])
            curr += (1 << i);
    }
    
    return nums[curr + 1];

}