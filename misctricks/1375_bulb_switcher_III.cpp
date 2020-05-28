/** Nathan Zhu Saturday, May 234, 2020 Stockton, CA. Watched lights out with Neha and Rak today.  Also went to apple store
 *  Leetcode 1375 | medium | medium
 *  Category: misc tricks
 */




#include <vector>
using namespace std;
int numTimesAllBlue(vector<int>& light) {
    int ret(0), curr(0), right(0);
    
    for(auto l : light){
        right = max(l, right);
        curr += 1;
        if(curr == right) ret++;
    }
    
    return ret;
}