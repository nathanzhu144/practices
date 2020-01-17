/** Nathan Zhu January 4th, 2020
 *  Leetcode 479 | hard | hard
 *  I got this problem for my final question for wolverine trading.
*/
#include <string>

using namespace std;

long build(int n){
    string temp = to_string(n);
    return stol(temp + string(temp.rbegin(), temp.rend()));
}
int largestPalindrome(int n) {
    if(n == 1) return 9;
    
    int largest = pow(10, n) - 1;
    int smallest = pow(10, n - 1);
    
    for(int i = largest; i >= smallest; --i){
        long cand = build(i);
        
        for(long j = largest; j * j >= cand; j--){
            if(cand % j == 0 && cand / j <= largest && cand / j >= smallest){
                return cand % 1337;
            }
        }
        
    }
    return -1;
}