/* Nathan Zhu Friday Stockton, CA. 12:54 am June 19th, 2020.  Tomorrow is our 2nd anniversary. :)  50.24% of leetcode questions done.  Called everyone today
*                                                               Dom, Katelyn, Catherine, Amber, Wendy etc, etc. Good seeing everyone again.  Everyone's changed so much you know?  
*  Leetcode 668 | hard | hard
*  Category: binary search
*/


#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <set>
#include <string>
#include <queue>
#include <deque>
#include <utility>
#include <algorithm>
#include <cmath>
#include <limits>
#include <iostream>

using namespace std;


int findKthNumber(int m, int n, int k) {
    int left(0), right(m * n), ret(-1);
    
    while(left <= right){
        int mid = (right - left) / 2 + left;
        if(count(mid, m, n) >= k){
            ret = mid;
            right = mid - 1;
        }
        else left = mid + 1;
    }
    return ret;
}

// counts how many numbers are <= target in this array in O(C) time.
int count(int target, int r, int c){
    int ret(0);
    for(int i = 1; i <= c; ++i){
        ret += min(r, target / i);   // we need the min here becuse for some numbers greater than number of rows, 
                                     // we want to cap out at r.
    }
    return ret;
}