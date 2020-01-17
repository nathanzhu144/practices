/** Nathan Zhu 10:05 pm, Tuesday December 31st, 2019, last 2 hours of this decade.  Went to Santa Cruz boardwalk, won 2 medium stuffed animals and 3 small ones,
 *                                                    all in balloon popping with water.  I am good.  Won 5/7 times I played.
 *  Leetcode 1249 | medium | medium
 *  Category: Stack / BFS
 *  
 *  BFS would work correctly, but is too slow.
 *  Stack is O(N) time, and greedily matches parens.
 *  Intuition is we have a stack of indices to characters, and at the very end, whatever indices remain on our stack
 *  are invalid characters that have to be removed (we replace them with a star).  Then, we remove them.
 *  
 * */
#include <algorithm>
#include <stack>
#include <string>

using namespace std;


string minRemoveToMakeValid(string s) {
    stack<int> st;
    
    for(int i = 0; i < s.size(); ++i){
        if(s[i] == '(') st.push(i);
        if(s[i] == ')'){
            if(!st.empty() and s[st.top()] == '(') st.pop();  // only valid if stack is not empty and top of stack is correct bracket.
            else st.push(i);                                  // not valid end parens if it doesn't match an opening bracket, we will later remove this parens
        }
    }
    
    // replace all invalid parens with "*" for removal
    while(!st.empty()){
        int i = st.top();
        s[i] = '*';
        st.pop();
    }
    
    // remove all chars with *
    s.erase(std::remove(s.begin(), s.end(), '*'), s.end());
    return s;
}