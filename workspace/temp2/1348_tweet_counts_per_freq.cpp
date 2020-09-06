
/* Nathan Zhu  Monday July 20th, 2020 10:17 pm Stockton, CA.  Emailed Katie & Jaewon today.
*  Leetcode 1348 | medium | medium
*  Category: design
*
*  Good use of a set helps in this case. 
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

using namespace std;



class TweetCounts {
private:
    unordered_map<string, multiset<int>> table;
public:
    TweetCounts() {
    }
    
    void recordTweet(string tweetName, int time) {
        table[tweetName].insert(time);
    }
    
    vector<int> getTweetCountsPerFrequency(string freq, string tweetName, int startTime, int endTime) {
        int time = 24 * 3600;
        if(freq[0] == 'm') time = 60;
        if(freq[0] == 'h') time = 60 * 60;
        int duration = endTime - startTime;
        
        vector<int> ret(duration / time + 1);
        const auto s = table.find(tweetName);
        if(s == table.end()) return ret;
        for(auto i = s->second.lower_bound(startTime); i != s->second.end() && *i <= endTime; i = next(i)){
            ret[(*i - startTime) / time]++;
        }
        return ret;
    }
};
