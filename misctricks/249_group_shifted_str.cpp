/** Nathan Zhu April 14th, 2020 Guy from Stanford told me to do more leetcode today.  Good stuff.
 *  Leetcode 249 | medium | easy
 *  Category: Making the hash is maybe the hardest part of this question.
 * 
*/

#include <algorithm>
#include <unordered_map>
#include <string>
#include <vector>

using namespace std;


string hashing(string& s){
    string ret;
    
    for(int i = 0; i < s.size() - 1; ++i){
        int num = (s[i + 1] - s[i] + 26) % 26;
        ret += to_string(num);
        ret += ".";
    }
    return ret;
}

vector<vector<string>> groupStrings(vector<string>& strings) {
    unordered_map<string, vector<string>> table;
    vector<vector<string>> ret;
    
    for_each(begin(strings), end(strings), [&](string& s){ table[hashing(s)].push_back(s); });
    for_each(begin(table), end(table), [&](auto& pr){ ret.push_back(pr.second);});
    return ret;
}