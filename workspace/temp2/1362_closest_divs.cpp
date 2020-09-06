
/* Nathan Zhu  Saturday July 18th, 2020  10:45 am   Had to cancel hot pot with Tan, Hiro, and co for today.  Coronavirus ya know? 
*  Leetcode 1362 | medium | medium
*  Category: math?
*  Runtime: sqrt(N)
*
*  Why do we return n + 1 over n + 2?  For numbers for which (n + 1) % i == 0 and (n + 2) % i == 0, n + 1 is closer to i.
*  This is true for cases like i = 1.
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


vector<int> closestDivisors(int num) {
    for(int i = pow(num + 2, 0.5); i > 0; --i){
        if((num + 1) % i == 0) return {(num + 1) / i, i};
        if((num + 2) % i == 0) return {(num + 2) / i, i};
    }
    return {0, 0}; // should not run, all nums are div by 1
}