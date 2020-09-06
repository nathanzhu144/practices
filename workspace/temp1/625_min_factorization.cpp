/* Nathan Zhu Monday Stockton, CA. 12:17 am June 22nd, 2020.  I watched a william lin video of him doing 150 questions in 12 hours lol.  OK my dude.
*  Leetcode 625 | medium | medium
*  Category:  Math, checking overflow cases.
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


// If there is a prime factor greater than 9, a will end up as
// not 1.
// There also is the special case for a == 1, 0 where we return the 
// respective number.
// We check for 10 digits or more to see if greater than 10 billion, but
// some 9 digit numbers are also greater than int_MAX.
int smallestFactorization(int a) {
    long num = 0;
    if(a < 2) return a;

    for(int div = 9, digits = 0; div >= 2; --div){
        while(a % div == 0){
            num += pow(10, digits++) * div;
            a /= div;
            if(digits >= 10) return 0;
        }
    }
    
    return (num >= INT_MAX || a != 1) ? 0 : int(num);
    }