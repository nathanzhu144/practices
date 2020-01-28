/* Nathan Zhu Jan 25th, 2020 10:52 pm, We watched hell's kitchen today at foundry with rak and crew.
*  Leetcode 732 | hard | damn hard yo
*  Category: Map
*  The map solution is so beautiful.  Can't believe this is a hard question.
*/

#include <map>
#include <algorithm>
using namespace std;

class MyCalendarThree {
public:
    MyCalendarThree() {
        
    }
    
    map<int, int> times;
    
    int book(int start, int end) {
        times[start]++;
        times[end]--;
        
        int ret = 0;
        int curr = 0;
        
        for(auto &pr:times){
            curr += pr.second;
            ret = max(curr, ret);
        }
        return ret;
    }
};
