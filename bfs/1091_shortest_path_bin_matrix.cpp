/* Nathan Zhu May 8th, 2020 STarting Salesforce a week-ush.
*  Leetcode 1091 | medium | damn, learned how to hash a vector today lmao
*  Category: BFS
*
*  Wrote my own hashing function lmao
*/


#include <vector>
#include <unordered_set>

using namespace std;


struct VHash{
    int operator()(const vector<int>& vec) const{
        int ret = 0;
        for(auto i : vec) ret ^= i;
        return ret;
    }
};


vector<vector<int>> get_neighbors(vector<vector<int>>& grid, int r, int c){
    vector<int> dr = {1, 0, -1, 0, 1, 1, -1, -1};
    vector<int> dc = {0, 1, 0, -1, 1, -1, -1, 1};
    vector<vector<int>> ret;
    
    for(int i = 0; i < dc. size(); ++i){
        int newr = dr[i] + r, newc = dc[i] + c;
        if(0 <= newr and newr < grid.size() and 0 <= newc and newc < grid[0].size() and grid[newr][newc] == 0){
            vector<int> pr = {newr, newc};
            grid[newr][newc] = 1;
            ret.push_back(pr);
        }
    }
    
    return ret;
    
}
    
int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
    unordered_set<vector<int>, VHash> visited;
    
    
    vector<vector<int>> q;
    if(grid[0][0] == 0) q.push_back({0, 0});
    int ret = 1;
    
    while(q.size()){
        vector<vector<int>> newq;
        
        for(auto& vec : q){
            int r = vec[0], c = vec[1];
            if (r == grid.size() - 1 and c == grid[0].size() - 1) return ret;
            for(auto& neigh : get_neighbors(grid, r, c)){
                if(visited.count(neigh)) continue;
                visited.insert(neigh);
                newq.push_back(neigh);
            }
            
        }
        ret += 1;
        q = vector<vector<int>>(newq.begin(), newq.end());
    }
    
    return -1;
    
    
}