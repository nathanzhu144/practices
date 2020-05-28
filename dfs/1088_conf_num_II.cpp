/* Natan Zhu May 16th, 2020
*  Leetcode 1088 | hard | kinda hard to think of this approach
*  category: Fizzbuzz
*
*  Ok, the idea here is two-fold.
*  First, a confusing number cannot contain 2, 3, 4, 5, 7, so confusing numbers are actually
*  pretty sparse.  It might be a bad idea to go through all numbers and check them.  If possible, we should
*  manually generate them.
*
*  Second, when we are generating the number, we can easily generate its complement, but appending a number with the 
*  appropriate base on.
*
*  Ex. 6, 9 are opposites.  69 is simply 6 * 10 + 9.  However, 96 is 9 * 10 + 6.
*                           We can distill this into an algorithm by representing 10 as a base, which gets multiplied by 10 on every recursive call.
*                           We can furthermore pass the number, and its reverse thru every recursive call.
*                           Everytime a number != its reverse, we increment by 1.
*/

#include <vector>
#include <unordered_map>

using namespace std;


vector<int> valid = {0, 1, 6, 8, 9};
unordered_map<int, int> translate = {
    {0, 0},
    {1, 1},
    {6, 9},
    {9, 6},
    {8, 8}
};

int helper(long curr, long rotation, long base, int N){
    int ret = 0;
    
    if(curr != rotation){
        ++ret;
    }
    
    for(auto num : valid){
        if(num == 0 and rotation == 0) continue;
        if(curr * 10 + num <= N) ret += helper(curr * 10 + num, translate[num] * base + rotation, base * 10, N);
    }
    return ret;
}


int confusingNumberII(int N) {
    return helper(0, 0, 1, N);
}