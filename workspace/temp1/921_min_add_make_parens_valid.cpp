/* Nathan Zhu Wednesday, Stockton, CA. 8:40 am, June 17th, 2020.
*  Leetcode 921 | medium| EZ
*  Category: stack?  I don't need a stack cuz there is only one type of parens.
*/


#include <vector>
#include <unordered_map>
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


int minAddToMakeValid(string S) {
    int count(0), ret(0);
    for(auto ch : S){
        if(ch == '(') ++count;
        else --count;
        if(count == -1){
            count = 0;
            ++ret;
        }
    }
    return ret + count;
}