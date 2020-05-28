/* Nathan Zhu Saturday May 16th, 2020 Weekly contest
*  Leetcode 1450 | easy | medium?
*  Category: Line sweep
*  I had to pull out a C++ map data structure for this one, so I don't think it is that easy lol
*  
*/

#include <map>
#include <vector>

using namespace std;

int busyStudent(vector<int>& start, vector<int>& end, int query) {
    int N = end.size();
    map<int, int> starts;
    map<int, int> ends;
    for(int i = 0; i < N; ++i){
        starts[start[i]] += 1;
        ends[end[i]] += 1;
    }
    
    int ret = 0;  // important
    int tot = 0;
    for(int i = 0; i <= 1000; ++i){
        tot += starts[i];
        if(query >= i) ret = tot;
        tot -= ends[i];
    }
    
    return ret;
}