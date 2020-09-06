/* Nathan Zhu Stockton, Ca, Saturday May 23rd, 2020, Went to apple store today
*  Leetcode 317 | hard | hard
*  Category: BFS
*/
#include <vector>
#include <utility>
#include <limits>
#include <set>
using namespace std;

int shortestDistance(vector<vector<int>>& grid) {
    if(!grid.size() || !grid[0].size()) return -1;
    int R(grid.size()), C(grid[0].size());
    vector<vector<int>> table(R, vector<int>(C, 0));
    vector<vector<int>> can_reach(R, vector<int>(C, 0));
    int num_b = 0;
    vector<pair<int, int>> moves = {pair(1, 0), pair(0, 1), pair(-1, 0), pair(0, -1)};
    
    for(int r = 0; r < R; ++r){
        for(int c = 0; c < C; ++c){
            if(grid[r][c] == 1) num_b++;
        }
    }
    
    for(int r = 0; r < R; ++r){
        for(int c = 0; c < C; ++c){
            if(grid[r][c] == 1){
                set<int> visited;
                vector<pair<int, int>> q = {pair(r, c)};
                int level(0), found_buildings(0);
                while(q.size()){
                    vector<pair<int, int>> newq;
                    
                    for(auto[r, c] : q){
                        table[r][c] += level;
                        for(auto[dr, dc] : moves){
                            int newr(dr + r), newc(dc + c);
                            int mapping = newr * C + newc;
                            if(newr < 0 || newc < 0 || newr >= R || newc >= C || visited.count(mapping)) continue;
                            visited.insert(mapping);
                            if(grid[newr][newc] == 1) found_buildings++;
                            else if(grid[newr][newc] == 0){
                                can_reach[newr][newc]++;
                                newq.emplace_back(newr, newc);
                            }
                        }
                    }
                    level++;
                    q = newq;
                    
                }
                if(found_buildings != num_b) return -1;
            }
        }
    }
    
    int ret = numeric_limits<int>::max();
    for(int r = 0; r < R; ++r){
        for(int c = 0; c < C; ++c){
            if(grid[r][c] == 0 && can_reach[r][c] == num_b) ret = min(ret, table[r][c]);
        }
    }
    return ret;
}