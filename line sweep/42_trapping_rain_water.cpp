/* Nathan Zhu Jan 28th, 2019 I like this question. After winter career fair, got interview with salesnow today.
*  Leetcode 42 | hard | not bad
*
*  Category: Misc tricks
*  Runtime : O(N), space O(N)
*/
#include <iostream>
#include <vector>

using namespace std;


int trap(vector<int>& height) {
    int N = height.size();
    vector<int> left(height.begin(), height.end());
    vector<int> right(height.begin(), height.end());
    
    for(int i = 1; i < N; ++i){
        left[i] = max(left[i], left[i - 1]);
    }
    for(int i = N - 2; i >= 0; --i){
        right[i] = max(right[i], right[i + 1]);
    }
    
    
    int ret = 0;
    for(int i = 0; i < N; ++i){
        ret+= min(left[i], right[i]) - height[i];
    }
    return ret;
}