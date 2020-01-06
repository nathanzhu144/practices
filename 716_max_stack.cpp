/**
 * Nathan Zhu January 4th, 2019 11:30 am
 * Leetcode 716 | easy | not at all easy
 * Category: Design (similar to LRU cache idea)
 * 
 * One edge case that is easy to miss is when you remove an element in pop or popmax, 
 * and it is the only element of that value, you should also remove the map entry in table.  
 * Otherwise, future calls to get_max will be wrong, as they can show that value even when it isn't there 
 * anymore.
 */

#include <list>
#include <vector>
#include <map>

using namespace std;

class MaxStack {
public:
    list<int> stk;
    map<int, vector<list<int>::iterator>> table;
    
    /** initialize your data structure here. */
    MaxStack() {
        
        
    }
    
    void push(int x) {
        stk.push_back(x);
        table[x].push_back(std::prev(stk.end()));
        
    }
    
    int pop() {
        int remove = stk.back();
        table[remove].pop_back();
        if(table[remove].empty()) table.erase(remove);
        stk.pop_back();
        return remove;
    }
    
    int top() {
        return stk.back();
    }
    
    int peekMax() {
        return table.rbegin()->first;
    }
    
    int popMax() {
        int remove_num = table.rbegin()->first;
        list<int>::iterator remove_it = table[remove_num].back();
        stk.erase(remove_it);
        table[remove_num].pop_back();
        
        if(table[remove_num].empty()) table.erase(remove_num);
        return remove_num;
    }
};