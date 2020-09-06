/* Nathan Zhu Friday Stockton, CA. 10:41 pm June 19th, 2020.  Day off on Friday today. :)
*  Leetcode 684 | medium | kinda hard?
*  Category: find first edge when added in which causes a cycle
*            This works cuz we are guaranteed at most one tree problem.
*
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

class UF{
public:
    void try_make(int i){
        if(!parent.count(i)) parent[i] = i;
    }
    
    int find(int n){
        if(parent[n] != n) parent[n] = find(parent[n]);
        return parent[n];
    }
    
    bool join(int a, int b){
        auto p1(find(a)), p2(find(b));
        if(p1 == p2) return false;
        parent[p1] = p2;
        return true;
    }
private:
    unordered_map<int, int> parent;
};


class Solution {
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        auto u = UF();
        for(auto& vec: edges){
            auto from(vec[0]), to(vec[1]);
            u.try_make(from);
            u.try_make(to);
            if(!u.join(from, to)) return {from, to};
        }
        return {};
    }
};