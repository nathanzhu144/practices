/* Nathan Zhu May 10th, 2020 Starting work at Salesforce next week!  Native exotics order for a bunch of veitchii seedlings came yesterday
*  Leetcode 943 | medium | have to think a bit
*  Category: Stack
*
*/
#include <vector>
#include <stack>
using namespace std;
// Why does greedy work?
// When we have 2 at the top of the stack, if we need to pop
// that value next, we must do it now. Any subsequent push will
// make the top of the stack different from 2, and we will never
// be able to pop 2 at this point again.

bool validateStackSequences(vector<int>& pushed, vector<int>& popped) {
    stack<int> stk;
    int i = 0;
    
    for(auto num : pushed){
        stk.push(num);
        
        while(stk.size() and stk.top() == popped[i]){
            i++;
            stk.pop();
        }
    }

    return stk.empty();
    
    
}