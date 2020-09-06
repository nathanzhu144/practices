/* Nathan Zhu Monday Stockton, CA. 7:27 pm June 22nd, 2020. Presentations tomorrow for Salesforce.  Talked to Dara and Austin today.
*  Leetcode 388 | medium | medium
*  Category:  Stack
*/


#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <set>
#include <stack>
#include <string>
#include <queue>
#include <deque>
#include <utility>
#include <algorithm>
#include <cmath>
#include <limits>
#include <sstream>
#include <iostream>

using namespace std;


vector<string> split(string& input, char c){
    stringstream str(input);
    string buffer;
    vector<string> ret;
    while(getline(str, buffer, c)){
        ret.push_back(buffer);
    }
    return ret;
}

int lengthLongestPath(string input) {
    stack<int> st;
    int ret = 0;
    
    for(auto& str: split(input, '\n')){
        auto i = str.find_last_of('\t');
        int num_tabs = (i == string::npos) ? 0 : i + 1;
        string rest = str.substr(num_tabs);
        
        // size 1 stack corresponds to 1 tabs
        // size k stack corresponds to k tabs
        while(st.size() > num_tabs) st.pop();
        
        // prefix is how many characters that are not '/' which
        // come before this file/folder.  If the stack is empty, prefix is 0.
        int prefix = (st.empty()) ? 0 : st.top();
        if(str.find('.') != string::npos){
            // st.top is len prefix
            // 1 is '/'
            // rest.size() is size of file not including tabs
            ret = max(ret, int(prefix + st.size() + rest.size())); 
        }
        else st.push(prefix + rest.size());
    }
    
    return ret;
}