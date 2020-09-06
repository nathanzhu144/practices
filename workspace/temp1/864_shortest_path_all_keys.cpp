/* Nathan Zhu Thursday Stockton, CA. 5:43, pm June 18th, 2020.  Tomorrow is our 2nd anniversary. :)  50.24% of leetcode questions done.  Called everyone today
*                                                               Dom, Katelyn, Catherine, Amber, Wendy etc, etc. Good seeing everyone again.  Everyone's changed so much you know?  
*  Leetcode 993 | easy | medium
*  Category: BFS
*/
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <set>
#include <string>
#include <queue>
#include <deque>
#include <utility>
#include <algorithm>
#include <cmath>
#include <limits>
#include <iostream>

using namespace std;


int shortestPathAllKeys(vector<string>& grid) {
    int R(grid.size()), C(grid[0].size());
    queue<int> q;
    int all_keys(0), ret(0);
    vector<vector<vector<bool>>> seen(R, vector<vector<bool>>(C, vector<bool>(64, false)));
    
    for(int r = 0; r < R; ++r){
        for(int c = 0; c < C; ++c){
            auto ch = grid[r][c];
            if(ch == '@'){
                q.push(r << 16 | c << 8);
                seen[r][c][0] = true;
            }
            if('a' <= ch && ch <= 'f'){
                all_keys |= 1 << (ch - 'a');
            }
        }
    }
    
    const vector<pair<int, int>> dirs= {pair(1, 0), pair(-1, 0), pair(0, 1), pair(0, -1)};
    while(q.size()){
        int size = q.size();
        while(size--){
            int curr = q.front(); q.pop();
            int r(curr >> 16), c((curr >> 8) & 0xFF), keys(curr & 0xFF);
            if(keys == all_keys) return ret;
            
            for(auto [dr, dc] : dirs){
                int newr(dr + r), newc(dc + c), newkeys(keys);
                if(newc < 0 || newr < 0 || newr >= R || newc >= C) continue;
                char newchar = grid[newr][newc];
                if(newchar == '#') continue;       //hit wall
                if('A' <= newchar && newchar <= 'F' && !((1 << (newchar - 'A')) & keys)) continue; // no key
                if('a' <= newchar && newchar <= 'f') newkeys |= (1 << (newchar - 'a'));            // new key
                if(seen[newr][newc][newkeys]) continue;                                            // visited
                q.push(newr << 16 | newc << 8 | newkeys);
                seen[newr][newc][newkeys] = true;
            }
        }
        ++ret;
    }
    return -1;
}