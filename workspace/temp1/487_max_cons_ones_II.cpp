/* Nathan Zhu Wednesday, Stockton, CA. 8:23 am, June 17th, 2020.
*  Leetcode 487 | medium | EZ
*  Category: sliding window
*/


#include <vector>
#include <unordered_map>
#include <set>
#include <queue>
#include <deque>
#include <utility>
#include <algorithm>
#include <cmath>
#include <limits>
#include <iostream>

using namespace std;

int findMaxConsecutiveOnes(vector<int>& nums) {
    int left(0), right(0), one_count(0), ret(0), N(nums.size());
    
    while(right < N){
        if(nums[right++] == 0) one_count++;
        while(left < right && one_count > 1){
            if(nums[left++] == 0) one_count--;
        }
        ret = max(ret, right - left);
    }
    
    return ret;
}