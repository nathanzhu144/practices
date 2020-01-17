/* Nathan Zhu December 24th, 2019 Did this on paper way to sugar bowl ski resort on December 21s, 2019
*  Leetcode 695 | medium | not too bad
*  Category: DFS / Stack / BFS
*  
*  Same as number islands, but we find the biggest one instead.
*  Easier to do recursively, I did iteratively.
*/

#include <vector>
#include <stack>

using namespace std;

int maxAreaOfIsland(vector<vector<int>>& grid) {
    
    if(!grid.size()) return 0;
    
    int ret = 0;
    int R = grid.size();
    int C = grid[0].size();
    
    for(int r = 0; r < R; ++r){
        for(int c = 0; c < C; ++c){
            if(grid[r][c] == 0) continue;
            
            stack<pair<int, int>> stk;
            
            stk.push(std::make_pair(r, c));
            int island_s = 0;
            grid[r][c] = 0;
            
            while(!stk.empty()){
                auto node = stk.top();
                stk.pop();
                island_s++;
                int row = node.first; 
                int col = node.second;
                
                vector<vector<int>> change = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
                for(auto vec : change){
                    int newr = vec[0] + row;
                    int newc = vec[1] + col;
                    
                    if(newr >= 0 and newr < R and newc >= 0 and newc < C and grid[newr][newc] == 1){
                        stk.push(std::make_pair(newr, newc));
                        grid[newr][newc] = 0;
                    }
                }
                
            } // while stack
            ret = max(ret, island_s);
        } // for
    } // for
    
    return ret;
} // maxareafunc
