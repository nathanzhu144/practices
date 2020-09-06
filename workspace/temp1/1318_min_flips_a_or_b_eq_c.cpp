/* Nathan Zhu Thursday, June 4th, 2020. Stockton, CA, 8:05 pm, called Kareen today. 
*  Leetcode 1318 | medium | medium
*  Category: bits
*/
#include <algorithm>
#include <vector>
#include <unordered_map>

using namespace std;


int minFlips(int a, int b, int target) {
    int curr(1), ret(0);
    while(curr <= a || curr <= b || curr <= target){
        if(target & curr) ret += (!(curr & a) && !(curr & b)) ? 1 : 0;
        else ret += int(bool(curr & a)) + int(bool(curr & b));
        curr <<= 1;
    }
    return ret;
}