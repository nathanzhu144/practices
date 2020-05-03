/** Nathan Zhu April 24th, 2020.  COVID 19, stockton, CA.  Dog incident near Trader joe happened today, sad day.
 *  Leetcode 301 | hard | not that bad
 *  Category: BFS
*/

using namespace std;

#include <set>
#include <string>
#include <vector>

bool valid(string s){
    int i = 0;
    for(auto ch: s){
        if(ch == '(') i++;
        if(ch == ')') i--;
        if(i < 0) return false;
    }
    return i == 0;
}

vector<string> removeInvalidParentheses(string s) {
    vector<string> q = {s};
    set<string> visited; 
    
    while(q.size()){
        vector<string> newq, ret;
        
        for(auto& s : q){
            if(valid(s)) ret.push_back(s);
        }
        if(ret.size()) return ret;
        
        for(auto& s: q){
            for(auto i = s.begin(); i != s.end(); i = next(i)){
                string newstr = string(s.begin(), i) + string(next(i), s.end());
                if(visited.count(newstr)) continue;
                visited.insert(newstr);
                newq.push_back(newstr);
            }
        }
        
        q = newq;
    }
    
    return {};
}