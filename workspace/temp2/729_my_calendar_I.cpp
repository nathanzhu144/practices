
/* Nathan Zhu Tuesday, June 30th, 2020  Only three days of work thsi week.  Tomorrow is like Friday?
*  Leetcode 729 | medium | medium
*  Category: Design
*/


#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <set>
#include <map>
#include <stack>
#include <string>
#include <queue>
#include <deque>
#include <utility>
#include <algorithm>
#include <cmath>
#include <limits>
#include <iostream>

using namespace std;


class MyCalendar {
    map<int, int> start_to_end;
public:
    MyCalendar() {
    }
    // Pos, if exits, points at smallest time interval starting at a greater or eq value
    // to inserted interval.
    //
    // 2 invalid cases.
    //
    // Case 1: Pos points to an interval, whose pos->start < [start, end]
    // Case 2: Pos points to an interval, where (--pos)->end > [start, end]
    bool book(int start, int end) {
        auto pos = start_to_end.lower_bound(start);
        if(pos != start_to_end.end() && pos->first < end) return false;
        if(pos != start_to_end.begin() && (--pos)->second > start) return false;
        start_to_end[start] = end;
        return true;
    }
};