/** Nathan Zhu Tuesday Jan 21st, 2019 5:26 pm. 
 *  Leetcode NaN | ? | harder medium
 * 
 *  This CAN INCLUDE negative numbers.  (But this assumes k > 0 I believe.)
 * 
 *  The insight here is that while we can find maximum subarray sum in O(N) time, 
 *  the reason that works is if we ever have a egative subarray leading up to an element, it is always optimal to just 
 *  begin a new sequence beginning at the next index.
 * 
 *  However, in this case, that negative portion can be the key to making a future subarray small enough
 *  to be less than k, but big enough to still be biggest subarray sum less than k.
 * 
 * 
 *  Insight:
 *  Presum + upper_bound for a NLogN solution.
 * 
 *  At any point in the array, we want to find the largest subarray sum equals K ending at that point.
 *  To do so, we want to find the smallest presum that is bigger than (presum - k), as this will minimize
 *  the positive distance to k.  
*/
#include <vector>
#include <set>
#include <algorithm>
#include <iostream>

using namespace std;

int max_subarray_sum_less_k(vector<int> arr, int k){
    set<int> nums; 
    nums.insert(0);
    int ret = 0, presum = 0;

    for(auto num : arr){
        presum += num;

        set<int>::iterator it = nums.upper_bound(presum - k);
        if (it != nums.end()) ret = max(presum - *it, ret);
        nums.insert(presum);
    }

    return ret;
}

int main(){
    cout << max_subarray_sum_less_k({2, -3, 4, 3, 2, 2, 1}, 5);
}