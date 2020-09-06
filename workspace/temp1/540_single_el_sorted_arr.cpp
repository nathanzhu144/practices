/* Nathan Zhu Monday Stockton, CA. 7:40 pm June 22nd, 2020. Saw a really good Parting vs Mana PvP game today.  Parting is soo good bro.
*  Leetcode 540 | medium | medium
*  Category: binary search
*/


#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <set>
#include <stack>
#include <string>
#include <queue>
#include <deque>
#include <utility>
#include <algorithm>
#include <cmath>
#include <limits>
#include <iostream>

using namespace std;

// NOTE: 
// CAN BE MISSING NUMBERS.
//
// [1, 1, 2, 3, 3, 4, 4, 8, 8]
//  0  1  2  3  4  5  6  7  8

// Find leftmost number whose first occurrence is on odd index.
// If does not exist, return last number in array, as that's the only case
// where this leftmost number doesn't occur.
// like below ex
// [1, 1, 2]
//  0  1  2
// 


int singleNonDuplicate(vector<int>& nums) {
    int ret(nums.size());
    int left(0), right(nums.size() - 1);
    while(left <= right){
        int mid = (right - left) / 2 + left;

        // Test is first occurrence of this number.
        int test = mid;
        if (mid > 0 && nums[mid] == nums[mid - 1]) test--;
        if(test & 1){
            ret = test;
            right = mid - 1;
        }
        else left = mid + 1;
    }
        
    return nums[ret - 1];
}