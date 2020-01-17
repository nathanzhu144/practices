/** Nathan Zhu January 2nd, 2019 9:03 am
 *  Leetcode 29 | medium | hard-ish
 *  
 *  Doing division without division, multiplicaiton, or addition.  
 *  So, we use bitshifting and subtraction!
 *   
 *  Note that  n << 1 is equivalent to n * 2
 *  Runtime (LogN *  logN)
 *  Keep in mind 2^10 - 1, which would be 9 + 8 + 7 + ... + 1
 */
#include <climits>
#include <cstdlib>

int divide(int dividend, int divisor) {
    bool pos = (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0);
    
    long dvd = labs(dividend);
    long dvs = labs(divisor);
    
    int ret = 0;
    
    // Handling conditions like:
    // 1. INT MIN, -1, should return INT_MAX
    if (divisor == 1) return dividend;
    else if(dividend == INT_MIN and divisor == -1) return INT_MAX; 
    
    while(dvd >= dvs){
        int curr = 1;
        long currdvs = dvs;
        long currdvd = dvd;
        
        while(currdvd >= currdvs << 1){
            currdvs <<= 1;
            curr <<= 1;
        }
        
        ret += curr;
        dvd = dvd - currdvs;
    }
    
    if(!pos) return -ret;
    return ret;

}