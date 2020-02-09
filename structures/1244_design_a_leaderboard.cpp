/* Nathan Zhu Jan 4th, 2020.  South Quad, ate dinner with Paul earlier.
*  Leetcode 1244 | medium | not bad
*  Category: Design.
*            Good application of a tree.
 */
#include <set>
#include <unordered_map>
#include <utility>

using namespace std;

class Leaderboard {
public:
    // playtoscore = hash table mapping players to their scores
    // scoretoplay = set<pairs> representing {player score, player},
    //               we need a pair, to allow for removals on resets, otherwise
    //               players with the same score can get confused for each other.
    Leaderboard() {
        
    }
    
    void addScore(int playerId, int score) {
        scoretoplay.erase(make_pair(playtoscore[playerId], playerId));
        playtoscore[playerId] += score;
        scoretoplay.insert(make_pair(playtoscore[playerId], playerId));
    }
    
    int top(int K) {
        int ret = 0;
        auto i = scoretoplay.rbegin();
        for(int j = 0; j < K; ++j, ++i){
            ret += i->first;
        }
        return ret;
    }
    
    void reset(int playerId) {
        scoretoplay.erase(make_pair(playtoscore[playerId], playerId));
        playtoscore[playerId] = 0;
    }
private:
    set<pair<int, int>>  scoretoplay;
    unordered_map<int, int> playtoscore;
};
