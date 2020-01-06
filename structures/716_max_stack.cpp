/*  Nathan Zhu
*   Leetcode 716 | easy | HARD who the hell thought this was an easy problem lol
*   Category: C++ map, Linked list, design
*   
*   Basically all ops except top are logn.
*      
*   The idea is that we keep the order of the stack in a doubly-linked list,
*   Luckily in C++, there is a DLL with a list.
*  
*   However, we also need to be able to grab the maximum element - therefore
*   we also use a C++ map, which can do updates and get max in LogN time.  
*   The map is a map of ints (values in stack) -> an ordered list of iterators
*   
*   Since when we pop_max with multiple maximum values necessitates us popping the 
*   one closer to the top of the stack, we always pop from the back of the vector
*   as the back of the vector has the most recent elements.
*   
*/

#include <algorithm>
#include <vector>
#include <list>
#include <map>

using namespace std;
class MaxStack {
private:
    list<int> v;
    map<int, vector<list<int>::iterator>> mp;
public:
    /** initialize your data structure here. */
    MaxStack() {
    }
    
    void push(int x) {
        v.push_back(x);
        mp[x].push_back(std::prev(v.end()));
    }
    
    int pop() {
        list<int>::iterator top_it = std::prev(v.end());
        int top_val = *top_it;
        
        mp[top_val].pop_back();
        
        if(mp[top_val].empty()) mp.erase(top_val);
        
        v.pop_back();
        return top_val;
    }
    
    int top() {
        return v.back();
    }
    
    int peekMax() {
        return mp.rbegin()->first;
    }
    
    int popMax() {
        int max_val = this->peekMax();
        list<int>::iterator erased_it = mp[max_val].back();
        
        mp[max_val].pop_back();
        if(mp[max_val].empty()) mp.erase(max_val);
        
        v.erase(erased_it);
        return max_val;
    }
};
