/** Nathan Zhu Tuesday Sept 23rd, 2019 2:37 pm with Johnny.
 * Leetcode 200 | medium | medium
 * 
 * Did the union find version of leetcode 200.
*/
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

class UF{
public:
    void make_island(string p){
        sizes[p] = 1;
        parent[p] = p;
    }
        
        
    void union_isle(string p, string q){
        p = find(p); q = find(q);
        
        if(p == q){ return; }
        
        //We have merged two islands
        num_islands--;
        
        // We ensure p is bigger or eq than q
        //if(size[p] < size[q]) std::swap(p, q);
        
        // q's parent now is p, p has more land now
        parent[q] = p;
        sizes[p] += sizes[q];
    }
    
    string find(string p){
        if(parent[p] != p){
            parent[p] = find(parent[p]);
        }
        return parent[p];
    } 
    
    int num_islands = 0;
    unordered_map<string, string> parent;
    unordered_map<string, int> sizes;
};

class Solution {
public:
    
    int numIslands(vector<vector<char>>& grid) {
        UF islands = UF();
        vector<pair<int, int>> delta = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        
        for(int row = 0; row < grid.size(); ++row){
            for(int col = 0; col < grid[0].size(); ++col){
                if(grid[row][col] == '1'){
                    string p = to_string(row) + "|" + to_string(col);
                    islands.make_island(p);
                    
                    for(int i = 0; i < delta.size(); ++i){
                        int drow = delta[i].first, dcol = delta[i].second;
                        int newrow = drow + row, newcol = dcol + col;
                        
                        // We need to union
                        string q = to_string(newrow) + "|" + to_string(newcol);
                        if(islands.parent.find(q) != islands.parent.end()) islands.union_isle(p, q);
                        
                    }
                }
            }
        }
        
        return islands.num_islands;
    }
};