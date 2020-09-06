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


// Intuition, we start with a rectangle spanning whole array; this is 
// largest possible base. In order to get a larger base, we need to increase
// the minimum height of both sides.
//
// In each iteration, we discard the smaller of two heights, as replacing the 
// larger height will still give us same overall area.
int maxArea(vector<int>& height) {
    int N(height.size());
    int left(0), right(N - 1), ret(0);
    
    while(left < right){
        int area = (right - left) * min(height[left], height[right]);
        ret = max(area, ret);
        if(height[left] <= height[right]) ++left;
        else --right;
    }
    return ret;
}