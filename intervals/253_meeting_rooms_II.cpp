/* Nathan Zhu Jan 25th, 2020 10:52 pm, We watched hell's kitchen today at foundry with rak and crew.
*  Leetcode 253 | medium | so cool man
*  Category: Map
*  The map solution is so beautiful.  Never done it this way before.
*/

#include <vector>
#include <map>
#include <algorithm>

using namespace std;

int minMeetingRooms(vector<vector<int>>& intervals) {
    map<int, int> meetings;
    
    for(auto &i :intervals){
        meetings[i[0]] += 1;
        meetings[i[1]] -= 1;
    }
    
    int ret = 0;
    int counter = 0;
    for(auto& pr : meetings){
        counter += pr.second;
        ret = max(ret, counter);
    }
    
    return ret;
}