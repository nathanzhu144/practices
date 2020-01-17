/* Nathan Zhu December 24th, 2019 Did this on paper way to sugar bowl ski resort on December 21s, 2019
*  Leetcode 71 | medium | not too bad
*  Category: Stack
*  
*  A few tricky cases, but basic stack problem.
*/

#include <string>
#include <vector>
#include <iostream>
#include <sstream>

using namespace std;
string simplifyPath(string path) {
    stringstream ss(path);
    vector<string> stk;
    string temp;
    
    while(getline(ss, temp, '/')){
        if(temp == "" or temp == ".") continue;
        else if(temp == ".." and !stk.empty()) stk.pop_back();  // we can push_back on stack if it is not empty
        else if(temp != "..") stk.push_back(temp);              // for case of invalid .., we don't push_back
    }
    
    if(stk.empty()) return "/";  // if no path, return "/"
    
    string ret = "";
    for(string& s: stk){
        ret += ("/" + s);
    }
    
    return ret;
    
}