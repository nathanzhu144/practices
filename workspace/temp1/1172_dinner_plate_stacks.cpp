/* Nathan Zhu Stockton, CA, May 12th, 2020. 6:45 am  Calling Sophie from Amex next week! 
*  Leetcode 1172 | hard | hard?
*  Category: Design
*  The basis of this problem is a clever use of a treemap to keep track of emty slots.
*/
#include <map>
#include <set>
#include <vector>

using namespace std;

class DinnerPlates {
    map<int, vector<int>> stacks;
    set<int> empty_slots;
    int cap;
    
public:
    // Invariants we keep after each op:
    // A stack of plate is only in stacks if it is non-empty
    // A slot is only in empty slots 
    DinnerPlates(int capacity) {
        cap = capacity;
    }
    
    void push(int val) {
        if(empty_slots.empty()) empty_slots.insert(stacks.size());
        int insertidx = *empty_slots.begin();
        stacks[insertidx].push_back(val);
        if(stacks[insertidx].size() == cap){
            empty_slots.erase(insertidx);
        }
    }
    
    int pop() {
        if(stacks.empty()) return -1;
        int remidx = stacks.rbegin()->first;
        int ret = stacks[remidx].back();
        stacks[remidx].pop_back();
        if(stacks[remidx].empty()) stacks.erase(remidx);
        return ret;
    }
    
    int popAtStack(int index) {
        if(!stacks.count(index)) return -1;
        int ret = stacks[index].back();
        stacks[index].pop_back();
        empty_slots.insert(index);
        if(stacks[index].empty()) stacks.erase(index);
        
        return ret;
    }
};

/**
 * Your DinnerPlates object will be instantiated and called as such:
 * DinnerPlates* obj = new DinnerPlates(capacity);
 * obj->push(val);
 * int param_2 = obj->pop();
 * int param_3 = obj->popAtStack(index);
 */