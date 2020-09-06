/* Nathan Zhu Tuesday Stockton, CA. 10:49 am June 23nd, 2020.  I watched a william lin video of him doing 150 questions in 12 hours lol.  OK my dude.
*  Leetcode 388 | medium | medium
*  Category: stack / design
*  You can either represent prefixes with a stack OR a hash table.
*  Hash table is easier in the sense that you dont need to pop bac.
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
#include <iostream>
#include <sstream>
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
    unordered_map<int, int> level_to_count;
    int ret = 0;
    
    for(const auto& str: split(input, '\n')){
        size_t i = str.find_last_of('\t');
        int level = (i == string::npos) ? 0 : i + 1;
        string curr = str.substr(level);
        
        int length = curr.size();
        // not a file
        if(find(begin(str), end(str), '.') == end(str)){
            level_to_count[level] = level_to_count[level - 1] + length;
        }
        // is a file
        else ret = max(ret, level_to_count[level - 1] + level + length);
        
    }
    return ret;
}