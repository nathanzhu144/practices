
/* Nathan Zhu Thursday Stockton, CA. 5:43, pm June 18th, 2020.  Tomorrow is our 2nd anniversary. :)  50.24% of leetcode questions done.  Called everyone today
*                                                               Dom, Katelyn, Catherine, Amber, Wendy etc, etc. Good seeing everyone again.  Everyone's changed so much you know?  
*  Leetcode 414 | easy | med?
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

// First soln
int thirdMax(vector<int>& nums) {
    long top(numeric_limits<long>::min()), mid(numeric_limits<long>::min()), bottom(numeric_limits<long>::min());
    
    for(auto num : nums){
        if (num == top || num == mid || num == bottom) continue;
        if(num > top){
            bottom = mid;
            mid = top;
            top = num;
        }
        else if(num > mid){
            bottom = mid;
            mid = num;
        }
        else if(num > bottom){
            bottom = num;
        }
    }
    
    return (bottom != numeric_limits<long>::min()) ? bottom : top;
}

// Alternate soln
int thirdMax(vector<int>& nums) {
    set<int> table;
    for(auto num : nums){
        table.insert(num);
        if(table.size() > 3) table.erase(table.begin());
    }
    
    return (table.size() == 3) ? *(table.begin()) : *(table.rbegin());
}