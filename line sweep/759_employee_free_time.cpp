/**  Nathan Zhu May 12th, 2020. Damn, the GRE sucks bro.  Stockton, CA.
 *   Leetcode 759 | hard | not at all bad
 *   Category: Line sweep
 * 
 *   I think this solution with line sweep is maybe more intuitive than the one where 
 *   you sort all of the intervals.  The only problem w this solution is that it does not take 
 *   advantage of the fact that employee schedules are pre-sorted.
 * 
 *   Otherwise, to take advanage of this, you can do it kinda like merging k-sorted linked lists
 *   but with intervals.
 * 
*/

#include <vector>
#include <map>
using namespace std;

class Interval {
public:
    int start;
    int end;

    Interval() {}

    Interval(int _start, int _end) {
        start = _start;
        end = _end;
    }
};


vector<Interval> employeeFreeTime(vector<vector<Interval>> schedule) {
    map<int, int> table;
    vector<Interval> ret;
    
    for(auto& employee_sched : schedule){
        for(auto& interv : employee_sched){
            table[interv.start]++;
            table[interv.end]--;
        }
    }
    
    int ct = 0;
    int next_start = -1;
    for(auto [k, v] : table){
        ct += v;
        if(ct == 0 and next_start == -1){
            next_start = k;
        }
        else if(ct != 0 and next_start != -1){
            ret.emplace_back(next_start, k);
            next_start = -1;
        }
    }
    
    return ret;
}