/* Nathan Zhu  Tuesday July 20th, 2020 5:37 pm Stockton, CA.  Made pot roast today.  
*  Leetcode 1370 | easy | easy
*  Category: simulation
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


string sortString(string s) {
    vector<int> chars(26, 0);
    int N(s.size());
    string ret;
    
    for(auto ch : s) chars[ch - 'a']++;
    
    while(ret.size() != N){
        for(int i = 0; i < 26; ++i) ret += string(--chars[i] >= 0 ? 1 : 0, 'a' + i);
        for(int i = 25; i >= 0; --i) ret += string(--chars[i] >= 0 ? 1 : 0, 'a' + i);
    }
    
    return ret;
}