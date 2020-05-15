/** Nathan Zhu April 14th, 2020 Guy from Stanford told me to do more leetcode today.  Good stuff.
 *  Leetcode 49 | medium | easy
 *  Category: O(N) time is possible with a bucket sort, since inputs are all lowercase.
 * 
*/

#include <algorithm>
#include <unordered_map>
#include <string>
#include <vector>

using namespace std;

string count_sort(string& s){
    vector<int> buckets(26, 0);
    string ret;
    
    for_each(begin(s), end(s), [&](char ch){ buckets[ch - 'a']++; });
    for(int i = 0; i < 26; ++i){
        while(buckets[i]--) ret += to_string(i + 'a');
    }
    return ret;
}

vector<vector<string>> groupAnagrams(vector<string>& strs) {
    unordered_map<string, vector<string>> groups;
    vector<vector<string>> ret;
    
    for_each(begin(strs), end(strs), [&](string& s){ groups[count_sort(s)].push_back(s); });
    for_each(begin(groups), end(groups), [&](auto pr){ ret.push_back(pr.second); });
    return ret;
}