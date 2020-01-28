/** Nathan Zhu January 27th, 2019 7:42 am
 *  Leetcode 56 | medium | damn I like this question
 *  I thought of this soln on my own :)
 * 
 *  Insights: Think about a C++ map.
 *            Think about soln for calender scheduling II or III
 * 
 *  This has same runtime, but is definitely different from the normal greedy soln.
*/
#include <vector>
#include <map>

using namespace std;

vector<vector<int>> merge(vector<vector<int>>& intervals) {
    map<int, int> table;
    
    for(auto& i: intervals){
        int start = i[0];
        int end = i[1];
        
        ++table[start];
        --table[end];
    }
    
    vector<vector<int>> ret;
    
    int start = -1;
    int end = -1;
    int presum = 0;
    for(auto& pr : table){
        presum += pr.second;
        // The structure of this is to ensure correctness for 
        // an empty interval like [7,7], we need both if statements to trigger.
        if(start == -1) start = pr.first;
        if(presum <= 0){
            vector<int> temp = {start, pr.first};
            ret.push_back(temp);
            start = -1;
            end = -1;
        }
    }
    return ret;
}