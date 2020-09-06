/* Nathan Zhu June 14th, 2020 Stockton, CA.  3:38 pm
*  Leetcode 907 | medium | medium
*  Category: Monotonic stack
**/

// How many subarrays have 3 as a minimum?
// [2, 9, 7, 8, 3, 4, 6, 1]
//  ^                    ^
// PLE                   NLE
// 4 possible start points [9, 7, 8, 3]
// 3 possible end points   [3, 4, 6]
// Therefore this affects 12 different subarrays.


#include <vector>
#include <cmath>
using namespace std;


int sumSubarrayMins(vector<int>& A) {
    int N(A.size());
    vector<pair<int, int>> l_st, r_st;   // <num, idx>
    vector<int> left(N, 0), right(N, 0);
    
    // Initialize
    for(int i = 0; i < N; ++i){
        right[i] = N - i;
        left[i] = i + 1;
    }
    
    // For each number we find distance to previous less element & next less element
    for(int i = 0; i < A.size(); ++i){
        // previous less
        while(!l_st.empty() && A[i] < l_st.back().first) l_st.pop_back();
        left[i] = (l_st.empty()) ? i + 1 : i - l_st.back().second;
        l_st.emplace_back(A[i], i);
        
        //next less
        while(!r_st.empty() && A[i] < r_st.back().first){
            right[r_st.back().second] = i - r_st.back().second; 
            r_st.pop_back();
        }
        r_st.emplace_back(A[i], i);
    }
    
    int ret(0), MOD(pow(10, 9) + 7);
    for(int i = 0; i < N; ++i){
        ret = (ret + left[i] * right[i] * A[i]) % MOD;
    }
    return ret;
}