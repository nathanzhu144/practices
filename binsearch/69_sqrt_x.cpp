/** Nathan Zhu May 9th, 2020. Leetcoding hard, Stockon CA.
 *  Leetcode 69 | easy | some edge cases
 *  Category: Bin search
 * 
 *  Simple binary search, but in C++ we need to watch out for 
 *  overflows and divisions by 0.
 * 
*/

int mySqrt(int x) {
    int left = 1, right = x;
    if(x == 0) return 0;
    
    int ret = -1;
    while(left <= right){
        int mid = (right - left) / 2 + left;
        if(mid <= x / mid){
            ret = mid;
            left = mid + 1;
        }
        else right = mid - 1;
    }
    return ret;
}