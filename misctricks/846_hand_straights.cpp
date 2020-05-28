/* Nathan Zhu May 17th, 2020 1:36 am
*  Leetcode 846 | medium | not bad
*  Category: map
*
*  Either start from smallest element or biggest element.
*/

#include <vector>
#include <map>
#include <algorithm>

using namespace std;

bool isNStraightHand(vector<int>& hand, int W) {
    map<int, int> table;
    int N = hand.size();
    if(N % W != 0) return false;
    
    
    for(auto item : hand) table[item]++;
    
    while(N){
        int top_val = table.rbegin()->first;
        
        vector<int> check;
        for(int i = 0; i < W; ++i) check.push_back(top_val - i);
        
        if(any_of(begin(check), end(check), [&](int n){ return table[n] <= 0; })) return false;
        
        for(int i = 0; i < W; ++i){
            int curr = top_val - i;
            table[curr] -= 1;
            if(table[curr] == 0) table.erase(curr);
        }
        N -= W;
    }
    
    return true;
}