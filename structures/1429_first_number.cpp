/* Nathan Zhu May 14th, 2020. Startes at salesforce in 4 days!!s
*  Leetcode 1429 | medium | kinda boring
*
*  The first solution is not O(1), but is amortized O(1).
*  The second solution is actually O(1).
*/
#include <deque>
#include <unordered_map>
#include <algorithm>
#include <list>
#include <vector>

using namespace std;

class FirstUniqueAmortizeO1 {
    deque<int> q;
    unordered_map<int, int> counts;
public:
    FirstUniqueAmortizeO1(vector<int>& nums) {
        for_each(begin(nums), end(nums), [&](int n){ add(n); });
    }
    
    int showFirstUnique() {
        while(q.size() and counts[q.front()] > 1) q.pop_front();
        return (q.empty()) ? -1 : q.front();
    }
    
    void add(int value) {
        counts[value]++;
        if(counts[value] == 1) q.push_back(value);

    }
};


class FirstUniqueO1 {
    list<int> q;
    unordered_map<int, list<int>::iterator> pos;
    unordered_map<int, int> counts;
public:
    FirstUniqueO1(vector<int>& nums) {
        for_each(begin(nums), end(nums), [&](int n){ add(n); });
    }
    
    int showFirstUnique() {
        return (q.empty()) ? -1 : q.front();
    }
    
    void add(int value) {
        counts[value]++;
        if(counts[value] == 2) q.erase(pos[value]);
        if(counts[value] == 1){
            q.push_back(value);
            pos[value] = prev(q.end());
        }
    }
};