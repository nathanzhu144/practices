/* Nathan Zhu Thursday, June 4th, 2020. Stockton, CA, 8:05 pm, called Kareen today. 
*  Leetcode 1319 | medium | medium
*  Category: Union find, tbh not sure how to do this if we had to find specific components which needed to be connected.
*
*  Intuition: Number subgraphs - 1 == number of changes.
*/

#include <vector>
#include <unordered_map>

using namespace std;

class UF{
public:
    UF() : tot(0) {}
    
    void try_make(int x){
        if(parent.count(x)) return;
        parent[x] = x;
        tot++;
    }
    
    int find(int x){
        if(parent[x] != x) parent[x] = find(parent[x]);
        return parent[x];
    }
    
    void join(int a, int b){
        auto p1(find(a)), p2(find(b));
        if(p1 == p2) return;
        tot--;
        parent[p1] = p2;
    }
    
    int get_comp() { return tot; }
private:
    int tot;
    unordered_map<int, int> parent;
};


int makeConnected(int n, vector<vector<int>>& connections) {
    if(connections.size() < n - 1) return -1;
    UF u;
    for(int i = 0; i < n; ++i) u.try_make(i);
    for(auto& vec : connections){
        auto to(vec[0]), from(vec[1]);
        u.join(to, from);
    }
    return u.get_comp() - 1;
}
