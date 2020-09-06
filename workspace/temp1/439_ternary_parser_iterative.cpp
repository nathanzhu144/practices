/* Nathan Zhu Sunday Stockton, CA. 7:57 am June 19th, 2020.  I watched a william lin video of him doing 150 questions in 12 hours lol.  OK my dude.
*  Leetcode 439 | medium | medium
*  Category:         Stack
*
*  This question is a lot easier when you realize you don't need to worry about parens.
*  Intuition: Go from back to front with a stack.  
*/


#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <set>
#include <string>
#include <queue>
#include <stack>
#include <deque>
#include <utility>
#include <algorithm>
#include <cmath>
#include <limits>
#include <iostream>

using namespace std;

// Itertive parser
string parseTernary(string expression) {
    int N(expression.size());
    stack<char> st;

    for(int i = N - 1; i >= 0; i--){
        char ch = expression[i];
        if(!st.empty() && st.top() == '?'){
            st.pop();  // pop ?
            char first = st.top(); st.pop();
            st.pop();  // pop :
            char second = st.top(); st.pop();
            if(ch == 'T') st.push(first);
            else st.push(second);
        }
        else st.push(ch);
    }
        
    return string(1, st.top());
}




// This is recursive parser.
string helper(string& expr, int& i){
    int N(expr.size());
    if(i + 1 < N && expr[i + 1] == '?'){
        int icpy = i;
        i += 2;
        string a = helper(expr, i);
        i += 2;
        string b = helper(expr, i);
        return expr[icpy] == 'T' ? a : b;
        
    }
    else return string(1, expr[i]);
}
string parseTernaryRecursive(string expression) {
    int i = 0;
    return helper(expression, i);
}