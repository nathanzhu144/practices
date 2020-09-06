/* Nathan Zhu Thursday Stockton, CA. 11:53, pm June 18th, 2020.  Tomorrow is our 2nd anniversary. :)  50.24% of leetcode questions done.  Called everyone today
*                                                               Dom, Katelyn, Catherine, Amber, Wendy etc, etc. Good seeing everyone again.  Everyone's changed so much you know?  
*  Leetcode 766 | easy | EZ
*  Category: misc tricks
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


// For regular question
bool isToeplitzMatrix(vector<vector<int>>& matrix) {
    if(!matrix.size() || !matrix[0].size()) return true;
    int R(matrix.size()), C(matrix[0].size());
    
    for(int r = 1; r < R; ++r){
        for(int c = 1; c < C; ++c){
            if(matrix[r][c] != matrix[r - 1][c - 1]) return false;
        }
    }
    return true;
}

// This one is slower, but works for the follow-up where we can only load up a partial row in memory.
// We hash all rows, cand check to see if the hashed value is the same.
bool isToeplitzMatrix(vector<vector<int>>& matrix) {
    unordered_map<int, int> table;
    if(!matrix.size() || !matrix[0].size()) return true;
    int R(matrix.size()), C(matrix[0].size());
    
    for(int r = 0; r < R; ++r){
        for(int c = 0; c < C; ++c){
            int key = r - c;
            if(table.count(key) && table[key] != matrix[r][c]) return false;
            else table[key] = matrix[r][c];
        }
    }
    return true;
}