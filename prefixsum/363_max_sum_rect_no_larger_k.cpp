/** Nathan Zhu  January 25th, 2019 3:52 pm
 *  Leetcode 363 | hard | effing hard yo
 *  Category: DP / presum 
 * 
 *  The question decomposes into two ideas:
 *  
 *  Finding maximum sum submatrix inside matrix (not on leetcode)
 *  Finding maximum subarray sum < K            (not on leetcode)
 * 
 *  With these two insights, the code is relatively trivial.
 */

#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <climits>

using namespace std;

int max_sum_rect(vector<vector<int>>& matrix, int k){
    if(matrix.size() == 0 or matrix[0].size() == 0) return 0;
    int R = matrix.size();
    int C = matrix[0].size();
    int ret = INT_MIN;

    for(int sc = 0; sc < C; ++sc){
        vector<int> cols(R, 0);
        for(int ec = sc; ec < C; ++ec){
            for(int r = 0; r < R; ++r) cols[r] += matrix[r][ec];

            set<int> nums;
            nums.insert(0);
            int presum = 0;

            for(int r = 0; r < R; ++r){
                presum += cols[r];
                set<int>::iterator it = upper_bound(nums.begin(), nums.end(), presum - k - 1);   // NOTE: Upper bound is not inclusive, hence -1
                if(it != nums.end()) ret = max(ret, presum - *it);
                nums.insert(presum);
            }
        }
    }
    return ret;
}