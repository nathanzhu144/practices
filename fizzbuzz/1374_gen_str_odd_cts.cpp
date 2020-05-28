/** Nathan Zhu Saturday, May 23d, 2020 Stockton, CA. Watched lights out with Neha and Rak today.  Also went to apple store
 *  Leetcode 1374 | easy | easy
 *  Category: Fizzbuzz
 */
#include <string>

using namespace std;

string generateTheString(int n) {
    if(n & 1){
        string ret;
        for(int i = 0; i < n; ++i) ret += 'a';
        return ret;
    }
    else{
        string ret = "b";
        for(int i = 0; i < n - 1; ++i) ret += 'a';
        return ret;
    }
}