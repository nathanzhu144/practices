/* Nathan Zhu Wednesday July 14th, 2020  On road near Manteca.  Going to go pick up a barbell from San Francisco
*  Deploying golang projects to Heroku is really fun.  D:
*  Leetcode 1304 | easy | easy
*  Category: math
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


vector<int> sumZero(int n) {
    vector<int> ret;
    for(int i = 0; i < n / 2; ++i){
        ret.push_back(i + 1);
        ret.push_back(-(i + 1));
    }
    if(n & 1) ret.push_back(0);
    return ret;
}