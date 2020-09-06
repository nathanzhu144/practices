/* Nathan Zhu Tuesday, Stockton, CA. 11:34 pm, June 16th, 2020 Called Sophie from Amex today.
*  Leetcode 468 | medium | many edge cases lol
*  Category: Misc tricks
*/

#include <algorithm>
#include <string>
#include <vector>
#include <iostream>
#include <sstream>

using namespace std;

// Edge cases:
// "111111111111111111111" (can cause overflow w enough ones)
// "..."                   (stoi exception on empty space)
// "1.1.1."                (enough dots, but after splitting we only get 3 things.)
string validIPAddress(string IP) {
    return valid_IP4(IP) ? "IPv4" : (valid_IP6(IP) ? "IPv6": "Neither");
}

bool valid_IP4(string str){
    if (count(begin(str), end(str), '.') != 3) return false;
    vector<string> parsed = split(str, '.');
    if (parsed.size() != 4) return false;
    
    for(auto s : parsed){
        if(s.size() == 0 || s.size() > 3) return false;
        if(s.size() > 1 && s[0] == '0') return false;
        if(any_of(begin(s), end(s), [](char c){ return !isdigit(c);})) return false;
        if(stoi(s) < 0 || stoi(s) > 255) return false;
    }
    return true;
}

bool valid_IP6(string str){
    if(count(begin(str), end(str), ':') != 7) return false;
    vector<string> parsed = split(str, ':');
    if(parsed.size() != 8) return false;
    for(auto s: parsed){
        string news;
        std::transform(begin(s), end(s), std::back_inserter(news), ::toupper);
        if(news.size() > 4 || news.size() == 0) return false;
        if(!all_of(begin(news), end(news), ::isalnum) || any_of(begin(news), end(news), [](char c){ return c >= 'A' && c <= 'Z' && c > 'F'; })) return false;
    }
    return true;
}


vector<string> split(string str, char delim){
    stringstream s(str);
    string buf;
    vector<string> ret;
    while(getline(s, buf, delim)) ret.push_back(buf);
    return ret;
}