/** May 4th, 2020 Stockton, CA.  No meeting thursday today at SF!
 *  Leetcode 1314 | medium | medium
 *  Category: prefix sum
 */

#include <vector>

using namespace std;

vector<vector<int>> matrixBlockSum(vector<vector<int>>& mat, int k) {
    if(!mat.size() || !mat[0].size()) return {};
    int R(mat.size()), C(mat[0].size());
    vector<vector<int>> prefix(R, vector<int>(C, 0));
    vector<vector<int>> ret(R, vector<int>(C, 0));
    
    for(int r = 0; r < R; ++r){
        for(int c = 0; c < C; ++c){
            prefix[r][c] += mat[r][c];
            if(r > 0) prefix[r][c] += prefix[r - 1][c];
            if(c > 0) prefix[r][c] += prefix[r][c - 1];
            if(r > 0 && c > 0) prefix[r][c] -= prefix[r - 1][c - 1];
        }
    }
    
    for(int r = 0; r < R; ++r){
        for(int c = 0; c < C; ++c){
            int topleftrow = max(0, r - k);
            int topleftcol = max(0, c - k);
            int toprightrow = min(R - 1, r + k);
            int toprightcol = min(C - 1, c + k);
            
            ret[r][c] += prefix[toprightrow][toprightcol];
            if(topleftrow > 0) ret[r][c] -= prefix[topleftrow - 1][toprightcol];
            if(topleftcol > 0) ret[r][c] -= prefix[toprightrow][topleftcol - 1];
            if(topleftrow > 0 && topleftcol > 0) ret[r][c] += prefix[topleftrow - 1][topleftcol - 1];
        }
    }
    
    return ret;
}