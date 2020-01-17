
/* Nathan Zhu December 24th, 2019 Did this on paper way to sugar bowl ski resort on December 21s, 2019
*  Leetcode 150 | medium | not-so-bad
*  Category: stack
*  
*  Evaluate RPN
*/

#include <string>
#include <vector>
#include <stack>
using namespace std;

int evalRPN(vector<string>& tokens) {
    stack<string> stk;
    
    for(string& t : tokens){
        //basically checks if a token is a number
        if(isdigit(t[0]) or (t[0] == '-' and t.size() > 1 and isdigit(t[1])))
            stk.push(t);
        else{
            int second = stoi(stk.top()); stk.pop();
            int first = stoi(stk.top()); stk.pop();
            
            int res = 0;
            
            if(t == "+") res = first + second;
            else if(t == "-") res = first - second;
            else if(t == "*") res = first * second;
            else if(t == "/") res = first / second;
            
            stk.push(to_string(res));
        }
    }
    
    return stoi(stk.top());
}