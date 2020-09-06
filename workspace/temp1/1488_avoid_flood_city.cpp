/* Nathan Zhu Monday Stockton, CA. 1:18 am June 22nd, 2020.  I watched a william lin video of him doing 150 questions in 12 hours lol.  OK my dude.
*  Leetcode 1488 | medium | kinda hard lol
*  Category: misc tricks
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


// Interesting,
// lower_bound(begin(free_days), end(free_days), last_wet[rain]);  RUNS IN O(N) Because not random access iterator
// free_days.lower_bound(last_wet[rain]);                          RUNS IN O(LOGN) time because it is a random access iterator.
// 

vector<int> avoidFlood(vector<int>& rains) {
    set<int> free_days;
    unordered_map<int, int> last_wet;
    int N(rains.size());
    vector<int> ret;
    
    for(int i = 0; i < N; ++i){
        int rain = rains[i];
        if(rain == 0){
            free_days.insert(i);
            ret.push_back(1);       // if necessary will come back and modify this later.
        }
        else{
            if(last_wet.count(rain)){
                auto it = free_days.lower_bound(last_wet[rain]); 
                if(it == free_days.end()) return {};    // not possible to avoid flood
                ret[*it] = rain;
                free_days.erase(it);
            }
            ret.push_back(-1);
            last_wet[rain] = i;
        }
    }
    
    return ret;
}