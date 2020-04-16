/*  Nathan Zhu April 14th, 2020. 6:00 pm. 
*   Leetcode 945 | medium | medium ?
*   Category: Union-find w path compression
*
*   This soln is pretty smart, even though I'm not sur if it is O(N)
*/
using namespace std;
#include <iostream>
#include <unordered_map>
#include <vector>

unordered_map<int, int> table;
int find(int x){
    return table[x] = table.count(x) ? find(table[x] + 1) : x;
}
int minIncrementForUnique(vector<int>& A) {
    if(!A.size()) return 0;
    int ret = 0;
    
    for(auto num: A)
        ret += (find(num) - num);

    return ret;
}