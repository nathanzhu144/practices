/* Nathan Zhu Stockton, CA, June 1st, 2020. 8:18 ams Tomorrow is the first day I start at Amex last year! :O
*  Leetcode 1329 | medium | medium
*  Category: misc tricks
*  Tricks: R + C and R - C can hash diagonals to same bucket
*          Sort buckets backwards, and pop bck to get next item
*/



#include <vector>
#include <algorithm>
#include <utility>
#include <unordered_map>

using namespace std;
vector<vector<int>> diagonalSort(vector<vector<int>>& mat) {
    if(!mat.size() || !mat[0].size()) return {};
    int R(mat.size()), C(mat[0].size());
    unordered_map<int, vector<int>> table;
    
    for(int r = 0; r < R; ++r){
        for(int c = 0; c < C; ++c){
            table[r - c].push_back(mat[r][c]);
        }
    }
    
    for(auto& [k, v] : table) sort(begin(v), end(v), std::greater<int>());
    
    for(int r = 0; r < R; ++r){
        for(int c = 0; c < C; ++c){
            mat[r][c] = table[r - c].back();
            table[r - c].pop_back();
        }
    }
    
    return mat;
}