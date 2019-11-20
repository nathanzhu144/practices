/* Nathan Zhu
*  Category: Design
*  Leetcode 232 | easy | EZ
*/

#include <stack>

using namespace std;


class MyQueue {
public:
    
    stack<int> input;
    stack<int> output;
    /** Initialize your data structure here. */
    MyQueue() {
    }
    
    /** Push element x to the back of queue. */
    void push(int x) {
        input.push(x);
    }
    
    void moving(){
        while(!input.empty()){
            int curr = input.top();
            input.pop();
            output.push(curr);
        }
    }
    /** Removes the element from in front of queue and returns that element. */
    int pop() {
        peek();
        int ret = output.top();
        output.pop();
        return ret;
    }
    
    /** Get the front element. */
    int peek() {
        if(output.empty()){
            while(!input.empty())
                output.push(input.top()), input.pop();
        }
        return output.top();
    }
    
    /** Returns whether the queue is empty. */
    bool empty() {
        return input.empty() && output.empty();
    }
};