/** Nathan Zhu April 17th, 2020.  The barbell weights came today, but the barbell hasn't yet.
 *  Leetcode 305 | hard | kinda hard?
 *  Category: Union find
 * 
 *  Simple union find problem
*/
#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>

using namespace std;


class UF{
private:
    unordered_map<string, string> parent;
    int num;
public:
    UF(): num(0) {}

    string find(string& node){
        if(parent[node] != node){
            parent[node] = find(parent[node]);
        }
        return parent[node];
    }

    void make_island(int r, int c){
        string node = get_string(r, c);
        if (parent.count(node)) return;  // this island already exists
        parent[node] = node;
        num++;

        vector<int> moves = {0, 1, -1};
        
        for(auto dr: moves){
            for(auto dc: moves){
                if((dr != 0 and dc != 0) or (dr == 0 and dc == 0)) continue;

                string other = get_string(dr + r, dc + c);
                if(!parent.count(other)) continue;  // other island doesn't exist
                unions(other, node);
            }
        }
    }

    void unions(string& a, string& b){
        if(find(a) == find(b)) return;
        parent[find(a)] = find(b);
        num--;
    }

    string get_string(int r, int c){
        return to_string(r) + " " + to_string(c);
    }

    int get_num_is(){ return num; }
};

class Solution {
public:
    vector<int> numIslands2(int m, int n, vector<vector<int>>& positions) {
        vector<int> ret;
        UF uf = UF();
        for(auto& i : positions){
            int r = i[0], c = i[1];
            uf.make_island(r, c);
            ret.push_back(uf.get_num_is());
        }
        return ret;
    }
};