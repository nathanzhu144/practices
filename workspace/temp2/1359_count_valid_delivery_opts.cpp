
/* Nathan Zhu  Monday July 20th, 2020 5:30 pm Stockton, CA.  Emailed Katie & Jaewon today.  Rank 2799 in number questions done, 812/1521
*  Leetcode 1359 | hard | hard
*  Category: DP
*
*  Saw this solution like a month ago, and figured it out on my own yesterday.  Kinda happy about this.
*/

#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <set>
#include <stack>
#include <string>
#include <queue>
#include <deque>
#include <utility>
#include <algorithm>
#include <cmath>
#include <limits>
#include <iostream>

using namespace std;


/*
n = 1
P1 D1
    
Total 1 way
    
    
n = 2 
    P1 D1
^  ^  ^  (possible insertion points for P2)
    
    
P2 P1 D1
    ^  ^  ^ 

P1 P2 D1
        ^  ^
P1 D1 P2 
        ^
            (Given insertion point of P2, how many insertion points for D2)
            
            (3 + 2 + 1) * 1 = 6
    
n = 3
    P1 P2 D1 D2
^  ^  ^  ^  ^

    P3 P1 P2 D1 D2
    ^  ^  ^  ^  ^
    P1 P3 P2 D1 D2
        ^  ^  ^  ^
        ...
    P1 P2 D1 D2 P3
                ^
            (Given insertion point of P3, how many insertion points for D3)
            
            (5 + 4 + 3 + 2 + 1) * 6
            = 90
    
    
Pattern: ways at N=i  ==  (ways at N=i-1) * (i * 2 - 1)
    
*/
    

    
int one_to_N(int N){
    return (N * (N + 1) / 2);
}
    
int countOrders(int N) {
    long ret = 1, MOD(pow(10, 9) + 7);
    
    for(int d = 2; d <= N; ++d){
        ret = (one_to_N(d * 2 - 1) * ret) % MOD;
    }
    return ret;
}