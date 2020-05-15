/** Nathan Zhu April 6th, 2020 3:00 am
 *  Leetcode 218 | hard | damn cool
 *  Category: Line sweep
 *  Runtime: NlogN
 * 
 *  Damn, I thought the divide and conquer soln was cool, but I don't mind this soln at all.
 *  The tie breaks are hairy tho for correct sorting of edges.
*/

#include <set>
#include <vector>
#include <algorithm>
#include <vector>
using namespace std;

struct VerticalEdge{
    int x;
    int y;
    bool is_start;

    bool operator<(VerticalEdge& other){
        if(x != other.x) return x < other.x;                                          // things with smaller x come first, as per line sweep
        else if(is_start != other.is_start) return is_start;                          // same x, one is start, one is end, we choose start first
        else if(!is_start) return y < other.y;                                        // same x, both are ends, we choose smaller ys first
        else return y > other.y;                                                      // same x, both are starts, we choose bigger yx first
    }
};

class Solution {
public:
    vector<vector<int>> getSkyline(vector<vector<int>>& buildings) {
        vector<VerticalEdge> edges;
        vector<vector<int>> ret;
        for(auto& bld: buildings){
            edges.push_back({bld[0], bld[2], true});
            edges.push_back({bld[1], bld[2], false});
        }

        sort(edges.begin(), edges.end());
        multiset<int> active = {0};         // import to have 0 here, as baseline is 0 height.
        int last_height = 0;
        for(auto& edge : edges){
            if(edge.is_start){
                active.insert(edge.y);
            }
            else{
                active.erase(active.find(edge.y));
            }
            int curr_height = *active.crbegin();
            if(curr_height != last_height){
                vector<int> curr = {edge.x, curr_height};
                ret.push_back(curr);
                last_height = curr_height;
            }
        }
        return ret;
    }
};