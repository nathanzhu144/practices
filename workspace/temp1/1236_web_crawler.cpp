/* Nathan Zhu Monday Stockton, CA. 12:17 am June 22nd, 2020.  I watched a william lin video of him doing 150 questions in 12 hours lol.  OK my dude.
*  Leetcode 1236 | medium | medium
*  Category:  BFS, but more annoying with only visiting things under the same hostname.
*/


#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <sstream>
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

using namespace std;

class HtmlParser{
public:
    vector<string> getUrls(string curr){ return {}; };
};

vector<string> split(string& s, char delim){
    stringstream strstr(s);
    vector<string> ret;
    string buf;
    while(getline(strstr, buf, delim)) ret.push_back(buf);
    return ret;
}

vector<string> crawl(string startUrl, HtmlParser htmlParser) {
    vector<string> ret;
    unordered_set<string> visited;
    deque<string> q;
    q.push_back(startUrl);
    string hostname = split(startUrl, '/')[2];
    
    while(q.size()){
        string curr = q.front(); q.pop_front();
        if(visited.count(curr) || split(curr, '/')[2] != hostname) continue;
        visited.insert(curr);
        ret.push_back(curr);
        for(auto link : htmlParser.getUrls(curr)) q.push_back(link);
    }
    
    return ret;
    
}