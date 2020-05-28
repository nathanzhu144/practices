/*  Nathan Zhu April 17th, 2020, Starting work at Salesforce tomorrow!
*   Leetcode 1381 | medium | not at all bad
*   Category: Design
*
*   I thought of using lazy propagation.  Apparently, many people couldn't come up with that idea.
*   I think I'm pretty smart :)
*/ 

#include <unordered_map>
#include <vector>

using namespace std;

class CustomStack {
    
    unordered_map<int, int> table;
    vector<int> stk;
    int max_size;
public:
    
    CustomStack(int maxSize) {
        max_size = maxSize;
    }
    
    void push(int x) {
        if(stk.size() < max_size){
            stk.push_back(x);
        }
    }
    
    int pop() {
        int N = stk.size();
        if(N == 0) return -1;
        
        int top = stk.back();
        stk.pop_back();
        if(table.count(N - 1)){
            if(N >= 2) table[N - 2] += table[N - 1];
            top += table[N - 1];
            table[N - 1] = 0;
        }
        
        return top;
    }
    
    void increment(int k, int val) {
        if(k >= stk.size()) k = stk.size();
        int inc_top = k - 1;
        
        table[inc_top] += val;
    }
};
