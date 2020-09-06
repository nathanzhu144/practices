/* Nathan Zhu Wednesday, Stockton, CA. 11:37 pm, June 17th, 2020.  Tomorrow is our 2nd anniversary. :)  Also, about to hit 50% of questions done on LC today.  49.9% rn!
*  Leetcode 881 | medium | medium
*  Category: sliding window
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


int numRescueBoats(vector<int>& people, int limit) {
    sort(begin(people), end(people));
    
    int left(0), right(people.size() - 1), ret(0);
    
    while(left <= right){
        if(people[left] + people[right] <= limit){
            ++left; --right;
        }
        else --right;
        ++ret;
    }
    return ret;
}