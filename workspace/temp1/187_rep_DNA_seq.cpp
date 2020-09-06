/* Nathan Zhu
*  Leetcode 187 | medium | medium
*  Category: Sliding window
*/

#include <vector>
#include <unordered_map>
#include <string>

using namespace std;

vector<string> findRepeatedDnaSequences(string s) {
    unordered_map<int, int> counts, mapping;
    unordered_map<int, string> actual;
    int curr(0), N(s.size());
    mapping[0] = 0;
    mapping['C' - 'A'] = 1;
    mapping['G' - 'A'] = 2;
    mapping['T' - 'A'] = 3;
    
    for(int i = 0; i < N; ++i){
        curr <<= 2;
        curr |= mapping[s[i] - 'A'];
        curr &= 0xFFFFF;
        
        if(i < 9) continue;
        if(!actual.count(curr)) actual[curr] = s.substr(i - 9, 10);
        counts[curr]++;
        if (counts[curr] > 2) counts[curr] = 2;   // prevent overflows.
    }
    
    vector<string> ret;
    for(auto [k, v] : counts){
        if(v == 2) ret.push_back(actual[k]);
    }
    return ret;
}