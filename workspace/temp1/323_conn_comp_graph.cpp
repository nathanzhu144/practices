/* Nathan Zhu Tuesday Stockton, CA. 12:35 am June 23nd, 2020.  I watched a william lin video of him doing 150 questions in 12 hours lol.  OK my dude.
*  Leetcode 323 | medium | easy?
*  Category: Union find
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


class UF{
public:
    UF(int n){
        parent = vector<int>(n, 0);
        for(int i = 0; i < n; ++i) parent[i] = i;
        num = n;
    }
    
    void join(int a, int b){
        int p1(find(a)), p2(find(b));
        if(p1 == p2) return;
        parent[p1] = p2;
        --num;
    }
    
    int find(int a){
        if(parent[a] != a) parent[a] = find(parent[a]);
        return parent[a];
    }
    vector<int> parent;
    int num = 0;
};


int countComponents(int n, vector<vector<int>>& edges) {
    auto u = UF(n);
    for(auto& vec: edges){
        u.join(vec[0], vec[1]);
    }
    return u.num;
}
