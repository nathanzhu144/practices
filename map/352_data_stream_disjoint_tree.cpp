/** Nathan Zhu April 18th, 2020. Downstairs, Stockton, CA. Weights came today.
 *  Leetcode 352 | hard | kind hard?
 *  Category: UF / Binary tree
 *  This particular implementation is done with a binary tree.
 * 
 *  addnum runs in LogN time
 *  get intervals runs in O(N) time
*/
#include <vector>
#include <set>
#include <map>
using namespace std;

class SummaryRanges {
    map<int, vector<int>> tree;
public:
    /** Initialize your data structure here. */
    SummaryRanges() {
    }
    
    // LogN
    void addNum(int val) {
        // Case 1: val is already considered, return
        if (tree.count(val)) return; 
        map<int, vector<int>>::iterator bigger = tree.lower_bound(val);
        map<int, vector<int>>::iterator smaller = (bigger == tree.begin()) ? tree.end() : prev(bigger);

        // Merge upper, mid, lower.
        if(bigger != tree.end() and smaller != tree.end() and smaller->second[1] == val - 1 and bigger->first == val + 1){
            smaller->second[1] = bigger->second[1];
            tree.erase(bigger); 
        }
        // Merge lower, mid
        else if(smaller != tree.end() and smaller->second[1] >= val - 1){
            smaller->second[1] = max(val, smaller->second[1]);
        }
        // Merge mid, upper
        // NOTE WE HAVE TO ERASE OLD INTERVAL, AS INTERVAL START MAY CHANGE.
        else if(bigger != tree.end() and bigger->second[0] <= val + 1){
            int start = min(val, bigger->second[0]);
            tree[start] = {start, bigger->second[1]};
            tree.erase(bigger);
        }
        // No merges possible, new interval
        else{
            tree[val] = {val, val};
        }
    }
    
    vector<vector<int>> getIntervals() {
        vector<vector<int>> ret;
        for(auto i: tree) ret.push_back(i.second);
        return ret;
    }
};