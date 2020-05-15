/*  Nathan Zhu Got above median by a decent amount on 376 Final!! 
*   Leetcode 966 | medium | medium
*   Category: Misc tricks
*/


#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>
#include <numeric>

using namespace std;

string lowerKey(string &s) {
    return accumulate(begin(s), end(s), string("_"), [](string k, char c) { return k + (char)tolower(c); });
}
string vowelKey(string &s) {
    return accumulate(begin(s), end(s), string(""), [](string k, char c) { return k +
    (char)(string("aeiou").find(tolower(c)) != string::npos ? '*' : tolower(c)); });
}
vector<string> spellchecker(vector<string>& wordlist, vector<string>& queries) {
    unordered_map<string, string> words;
    for (auto w : wordlist) {
    words.insert({ w, w }), words.insert({ lowerKey(w), w }), words.insert({ vowelKey(w), w });
    }
    vector<string> res;
    for (auto q : queries) {
    auto it = words.find(q);
    if (it == words.end()) it = words.find(lowerKey(q));
    if (it == words.end()) it = words.find(vowelKey(q));
    if (it != words.end()) res.push_back(it->second);
    else res.push_back("");
    }
    return res;
}