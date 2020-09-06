/* Nathan Zhu Tuesday August 18th 2020 Chicago, IL, Just got to chicago two days ago.
*  Leetcode 1347 | medium | easy
*  Category: misc trick
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

int search(vector<int>& nums, int target) {
    int N(nums.size());
    int left(0), right(N - 1);
    
    while(left <= right){
        int mid = (right - left) / 2 + left;
        
        // found target
        if(nums[mid] == target) return mid;
        
        // division is not between left & mid.
        else if(nums[left] <= nums[mid]){
            if(nums[left] <= target && target < nums[mid]) right = mid - 1;
            else left = mid + 1;
        }
        // division is not between right & mid.
        else{
            if(nums[mid] < target && target <= nums[right]) left = mid + 1;
            else right = mid - 1;
        }
    }
    return -1;
}