/* Nathan Zhu Jan 25th, 2020 10:52 pm, We watched hell's kitchen today at foundry with rak and crew.
*  Leetcode 731 | medium | damn hard yo
*  Category: Map
*  The map solution is so beautiful. 
*/

#include <map>

using namespace std;

class MyCalendarTwo {
public:
    map<int, int> delta;
    MyCalendarTwo() {
        
    }
    
    bool book(int start, int end) {
        delta[start]++;
        delta[end]--;
        
        int count = 0;
        
        for(auto& i : delta){
            count += i.second;
            
            if(count >= 3){
                delta[start]--;
                delta[end]++;
                return false;
            }
        }
        
        return true;
    }
};