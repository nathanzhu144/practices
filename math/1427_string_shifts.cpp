/*  Nathan Zhu April 14th, 2020.  2:55 pm.
*   Leetcode 1427 | easy | easy
*   Category: Math
*
*    think I had a question similar to this for goldman OA.
*   I don't have a good solution for making mods with negative work in C++.
*/

using namespace std;
#include <string>
#include <vector>

// To ensure modding w negative numbers works out,
// I keep adding until positive.
int make_pos(int num, int N){
    while(num < 0){
        num += N;
        N *= 2;
    }
    return num;
}

string stringShift(string s, vector<vector<int>>& shift) {
    int count(0), N(s.size());
    
    for(auto & vec: shift){
        if(vec[0] == 0) count += vec[1];
        else count -= vec[1];
    }
    
    int start = make_pos(count, N) % N;
    string ret;
    for(int i = 0; i < N; ++i){
        ret += s[(i + start) % N];
    }
    
    return ret;  
}