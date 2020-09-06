/* Nathan Zhu Saturday June 20th, 2020 Day off on Friday yesterday.  
*  Leetcode 261 | medium | medium
*  Category: BFS
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

// A tree is a minimally connected graph
// A tree is a connected acyclic graph
// We check for acyclic and minimally connected.

using namespace std;

class UF{
public:

void try_make(int x){
    if(!parent.count(x)) parent[x] = x;
}
int find(int x){
    if(parent[x] != x) parent[x] = find(parent[x]);
    return parent[x];
}

bool join(int a, int b){
    auto p1(find(a)), p2(find(b));
    if(p1 == p2) return false;
    parent[p2] = p1;
    return true;
}
private:
unordered_map<int, int> parent;
};

class Solution {
public:
bool validTree(int n, vector<vector<int>>& edges) {
    auto u = UF();
    for(auto vec : edges){
        auto from(vec[0]), to(vec[1]);
        u.try_make(from);
        u.try_make(to);
        if(!u.join(from, to)) return false;
    }
    return edges.size() == n - 1;
}
};