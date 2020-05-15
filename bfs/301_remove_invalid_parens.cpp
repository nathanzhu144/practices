/** Nathan Zhu April 24th, 2020.  COVID 19, stockton, CA.  Dog incident near Trader joe happened today, sad day.
*   Nathan Zhu May 9th, 2020.  A better day.
 *  Leetcode 301 | hard | not that bad
 *  Category: BFS
*/

using namespace std;

#include <set>
#include <string>
#include <vector>

bool valid_parens(string& s){
    int ctr = 0;
    for(auto ch: s){
        if(ch == '(') ctr += 1;
        if(ch == ')') ctr -= 1;
        if(ctr < 0) return false;
    }
    return ctr == 0;
}

class Solution {
public:
    vector<string> removeInvalidParentheses(string s) {
        vector<string> q = {s}, ret;
        set<string> visited;
        
        while(q.size()){
            vector<string> newq;
            if(any_of(q.begin(), q.end(), valid_parens)){
                std::copy_if(q.begin(), q.end(), back_inserter(ret), valid_parens);
                return ret;
            }
            
            for(auto str : q){
                for(int i = 0; i < str.size(); ++i){
                    string newstr = str.substr(0, i) + str.substr(i+1);
                    if(visited.count(newstr)) continue;
                    visited.insert(newstr);
                    newq.push_back(newstr);
                }
            }
            q = newq;
        }
        
        // should not get here.
        return ret;
    }
};
