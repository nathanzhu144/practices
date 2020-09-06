/* Nathan Zhu Tuesday July 14th, 2020  Stockton, CA. TACO TUESDAY
*  Deploying golang projects to Heroku is really fun.  :P
*  Leetcode 1494 | hard | hard??
*  Category: Bit tricks & DP
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


// works but in a real interview, can be replaced by __builtin_popcount(int n);
int get_set(int n){
    int ret = 0;
    while(n){
        n &= (n - 1);
        ret++;
    }
    return ret;
}

int minNumberOfSemesters(int n, vector<vector<int>>& dependencies, int k) {
    unordered_map<int, int> course_to_dep;
    vector<int> dp(1 << n, n + 1);
    dp[0] = 0;
    
    // convert from 1-index to 0-index
    for(auto& vec : dependencies){
        course_to_dep[vec[1] - 1] |= (1 << (vec[0] - 1));
    }
    
    // If we have two courses, n = 2
    // taken < 1 << 2
    // 0 0
    // 0 1
    // 1 0
    // 1 1
    // These should be all configurations of taken
    for(int taken = 0; taken < 1 << n; ++taken){
        int available = 0;
        
        // We want to make each bit of available set if it is a course that can be taken from
        // current prereqs, taken.  This is done with a bitwise and.
        for(int course = 0; course < n; ++course){
            if((course_to_dep[course] & taken) == course_to_dep[course]){
                available |= (1 << course);
            }
        }
        
        // do not retake courses, not doing this will make us reject valid course orders?
        available &= ~taken;
        
        // The loop below is a trick to iterate thru all subsets represented by bitmask available
        // 1 0 1 1 available
        // 
        // 1 0 1 0
        // 1 0 0 1
        // 1 0 0 0
        // 0 1 1 1 => 0 0 1 1
        // 0 0 1 0
        // 0 0 0 1
        // 0 0 0 0
        for(int subset = available; subset; subset = (available & (subset - 1))){
            if(get_set(subset) > k) continue;
            // any combination of courses (if less or equal than k) could be studied at this step
            // i | s means what we combine already studied courses before with courses we can study at the current step
            dp[taken | subset] = min(dp[taken | subset], dp[taken] + 1);
        }
        
    }
    
    return dp.back();
}