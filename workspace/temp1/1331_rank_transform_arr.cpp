/* Nathan Zhu Stockton, CA, June 1st, 2020. 8:18 ams Tomorrow is the first day I start at Amex last year! :O
*  Leetcode 1331 | easy | easy
*  Category: fizzbuzz
*/

#include <vector>
#include <map>
using namespace std;


vector<int> arrayRankTransform(vector<int>& arr) {
    map<int, vector<int>> table;
    vector<int> ret(arr.size(), 0);
    
    for(int i = 0; i < arr.size(); ++i){
        table[arr[i]].push_back(i);
    }
    
    int i = 1;
    for(auto [k, v] : table){
        for(auto idx : v) ret[idx] = i;
        i++;
    }
    
    return ret;
}