/** Nathan Zhu Saturday, May 23d, 2020 Stockton, CA. Watched lights out with Neha and Rak today.  Also went to apple store
 *  Leetcode 1380 | easy | easy
 *  Category: Fizzbuzz
 */


#include <vector>
#include <numeric>
#include <limits>
using namespace std;
vector<int> luckyNumbers (vector<vector<int>>& matrix) {
    if(!matrix.size() || !matrix[0].size()) return vector<int>();
    int R(matrix.size()), C(matrix[0].size());

    vector<int> rows(R, numeric_limits<int>::max());
    vector<int> cols(C, numeric_limits<int>::min());
    vector<int> ret;
    
    for(int r = 0; r < R; ++r){
        for(int c = 0; c < C; ++c){
            rows[r] = min(rows[r], matrix[r][c]);
            cols[c] = max(cols[c], matrix[r][c]);
        }
    }
    
    for(int r = 0; r < R; ++r){
        for(int c = 0; c < C; ++c){
            if(rows[r] == matrix[r][c] && cols[c] == matrix[r][c]){
                ret.push_back(matrix[r][c]);
            }
        }
    }
    
    return ret;
}