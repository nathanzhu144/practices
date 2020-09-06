
/* Nathan Zhu Tuesday July 14th, 2020 6:49 pm Stockton, CA. TACO TUESDAY
*  Deploying golang projects to Heroku is really fun.  :P
*  Leetcode 1483 | hard | hard
*  Category: Design, binary lifting
*
*  https://iq.opengenus.org/binary-lifting-k-th-ancestor-lowest-common-ancestor/#:~:text=Binary%20Lifting%20is%20a%20technique,two%20nodes%20in%20a%20tree
*
*  Idea is simple, but didn't think of it
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


class TreeAncestor {
private:
    vector<vector<int>> table;
    int POWER = 20;
public:
    TreeAncestor(int n, vector<int>& parent) {
        
        vector<vector<int>> t(parent.size(), vector<int>(POWER));
        
        for(int i = 0; i < parent.size(); ++i){
            t[i][0] = parent[i];
        }
        
        for(int j = 1; j < POWER; ++j){
            for(int i = 0; i < parent.size(); ++i){
                if(t[i][j - 1] == -1) t[i][j] = -1;
                else t[i][j] = t[t[i][j - 1]][j - 1];
            }
        }
        swap(t, table);
    }
    
    int getKthAncestor(int node, int k) {
        for(int i = 0; i < POWER; ++i){
            if((k >> i) & 1){
                node = table[node][i];
                if(node == -1) return -1;
            }
        }
        return node;
    }
};
