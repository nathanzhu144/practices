
/* Nathan Zhu  Tuesday July 20th, 2020 5:30 pm Stockton, CA.  Made pot roast today.  
*  Leetcode 1347 | medium | easy
*  Category: misc trick
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



int minSteps(string s, string t) {
    if(s.size() != t.size()) return -1;
    unordered_map<char, int> s_ct, t_ct;
    int ret(0), N(s.size());
    
    for(auto ch : s) s_ct[ch]++;
    for(auto ch : t) t_ct[ch]++;
    
    for(auto [s_ch, s_ch_ct] : s_ct){
        ret += min(s_ch_ct, t_ct[s_ch]);
    }
    
    return N - ret;
}