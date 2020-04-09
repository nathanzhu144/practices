/** Nathan Zhu March 16th, 2020 Monday, Coronavirus quarantine, Foundry Lofts
 *  Leetcode 50 | medium | not bad
 *  Category: Divide and conq
 */

// So, when taking a power smaller than 0, there are some numbers that cannot be converted to their positive equivalent.
// Specifically,
// 2147483646      is biggest num
// -2147483647     is smallest num
// 
// If the smallest num is converted to pos, it will overflow, so we do the soln below.


double myPow(double x, int n) {
    if(x == 1) return 1;
    if(n == 0) return 1;
    if(n == 1) return x;
    if(n < 0) return 1 / x * myPow(1 / x, -(n + 1));  // THIS IS IMPORTANT
    if(n & 1) return x * myPow(x, n - 1);
    double t = myPow(x, n / 2);
    return t * t;
}