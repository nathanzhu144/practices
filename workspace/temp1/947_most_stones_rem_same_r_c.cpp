/* Nathan Zhu Saturday Stockton, CA. 2:29 am June 20th, 2020.  Day off on Friday today. :)
*  Leetcode 947 | medium | hard
*  Category: UF
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
private:
    unordered_map<int, int> parent;
    int num_graphs;
public:
    UF(): num_graphs(0){}
    void try_make(int x){
        if(!parent.count(x)){
            parent[x] = x;
            ++num_graphs;
        }
    }
    
    int find(int x){
        if(parent[x] != x) parent[x] = find(parent[x]);
        return parent[x];
    }
    
    bool exists(int x){
        return parent.count(x);
    }
    
    bool join(int a, int b){
        auto p1(find(a)), p2(find(b));
        if(p1 == p2) return false;
        parent[p1] = p2;
        --num_graphs;
        return true;
    }
    
    int translate(int x, int y){
        return (x << 14) | y;
    }
    
    int get_graphs() { return num_graphs; }

};

class Solution {
public:
    int removeStones(vector<vector<int>>& stones) {
        int N(stones.size());
        auto u = UF();
        for(auto& vec: stones){
            u.try_make(u.translate(vec[0], vec[1]));
        }
        for(auto& vec1: stones){
            for(auto& vec2: stones){
                if(vec1 == vec2) continue;
                if(vec1[0] == vec2[0] || vec1[1] == vec2[1]){
                    int a = u.translate(vec1[0], vec1[1]);
                    int b = u.translate(vec2[0], vec2[1]);
                    u.join(a, b);
                }
            }
        }
        
        return N - u.get_graphs();
    }
};