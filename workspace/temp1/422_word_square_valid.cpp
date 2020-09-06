/* Nathan Zhu Wednesday, Stockton, CA. 11:19 pm, June 17th, 2020.  Tomorrow is our 2nd anniversary. :)  Also, about to hit 50% of questions done on LC today.  49.97% rn!
*  Leetcode 422 | easy | easy
*  Category: misc tricks
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



bool validWordSquare(vector<string>& words) {
    int R(words.size());

    for(int r = 0; r < R; ++r){
        for(int c = 0; c < words[r].size(); ++c){
            if(c >= words.size() || r >= words[c].size() || words[c][r] != words[r][c]) return false;
        }
    }
    return true;
}