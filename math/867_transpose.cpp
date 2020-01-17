/* Nathan Zhu Saturday December 28th, 2019 9:05 pm
 * Leetcode 867 | easy | easy
 * Finding transpose of a matrix is easy.
*/

#include <vector>
using namespace std;

vector<vector<int>> transpose(vector<vector<int>>& A) {
    if(!A.size()) return A;
    
    int R = A.size();
    int C = A[0].size();
    vector<vector<int>> ret(C, vector<int>(R, 0));
    
    for(int r = 0; r < R; ++r)
        for(int c = 0; c < C; ++c)
            ret[c][r] = A[r][c];
    
    return ret;
}