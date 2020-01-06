/* Nathan Zhu December 24th, 2019 Did this on paper way to sugar bowl ski resort on December 21s, 2019
*  Leetcode 224 | hard | yeah not too easy
*  Category: stack
*  
*  The tricky part here is the parens.  Since outside operators can modify the inside of a parens,
*  I use recursion to find the result of the parens and apply the outside operator to it.
*/

#include <string>
#include <utility>
using namespace std;

// Helper function returns pair (newidx, value from subexpression)
std::pair<int, int> helper(string s, int idx){
    int last_val = 0;
    bool pos = true;
    
    while(idx < s.size()){
        if(isdigit(s[idx])){
            int num = 0;
            while(idx < s.size() and isdigit(s[idx])){
                num = 10 * num + (s[idx] - '0');
                ++idx;
            }
            
            if(!pos) num = num * -1;
            
            last_val += num;
        }
        else if(s[idx] == '('){
            // ( means we need to do a recursive call to figure out expression in parens
            // with expression in parens, we can apply the sign, and then add it onto last_val
            std::pair<int, int> parens = helper(s, idx + 1);
            idx = parens.first;
            int num = parens.second;
            
            if(!pos) num = num * -1;
            
            last_val += num;
        }
        else if(s[idx] == '-'){
            pos = false;
            idx++;
        }
        else if(s[idx] == '+'){
            pos = true;
            idx++;
        }
        else if(s[idx] == ')'){
            return std::make_pair(idx + 1, last_val);
        }
        // in case of spaces and trash
        else idx++;
    }
    
    return std::make_pair(idx, last_val);
}

int calculate(string s) {
    auto ret = helper(s, 0);
    return ret.second;
}
