/* Nathan Zhu  Thursday July 16th, 2020  Hershal cancelled movie night this week!!! D:  
*  Leetcode 1253 | medium | medium
*  Category: Greedy
*
*
*/


#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <set>
#include <stack>
#include <string>
#include <queue>
#include <deque>
#include <utility>
#include <algorithm>
#include <cmath>
#include <limits>
#include <iostream>

using namespace std;




vector<vector<int>> reconstructMatrix(int upper, int lower, vector<int>& colsum) {
    int N(colsum.size());
    vector<vector<int>> ret = vector<vector<int>>(2, vector<int>(N, 0));
    for(int i = 0; i < N; ++i){
        if(colsum[i] == 2){
            upper--; lower--;
            ret[0][i] = 1; ret[1][i] = 1;
        }
        else if(colsum[i] == 1){
            if(upper > lower){
                ret[0][i] = 1;
                upper--;
            }
            else{
                ret[1][i] = 1;
                lower--;
            }
        }
        
        if(upper < 0 || lower < 0) return {};
    }
    return (upper > 0 || lower > 0) ? vector<vector<int>>() : ret;
    
}