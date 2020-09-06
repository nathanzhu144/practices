
/* Nathan Zhu  Thursday July 16th, 2020  Hershal cancelled movie night this week!!! D:  Had leetcode prep w Meera, Neha, Shazeen
*  Leetcode 1498 | medium | kinda hard
*  Category: sliding window, math
*
*  This solution was really smart.  Did not think of this one.
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



// What's going on here?
// Sort all the numbers, and do a sliding window.
// The idea is fix the leftmost number in the sliding window
// as a number that "has" to be in this subsequence.  Then, if there are
// N numbers between left and right, we know there are 2^(N-1) subsequences
// with left fixed.

int numSubseq(vector<int>& nums, int target) {
    sort(begin(nums), end(nums));
    int N(nums.size()), MOD(pow(10, 9) + 7);
    vector<int> powers = vector<int>(N, 0);
    
    powers[0] = 1;
    for(int i = 1; i < N; ++i){
        powers[i] = powers[i - 1] * 2;
        powers[i] %= MOD;
    }
    
    int ret = 0;
    
    int left(0), right(N - 1);
    while(left <= right){
        if(nums[left] + nums[right] > target) right--;
        else{
            ret = ret + powers[right - left];
            ret %= MOD;
            left++;
        }
    }
    return ret;
}