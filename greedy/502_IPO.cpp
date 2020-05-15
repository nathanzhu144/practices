/* Nathan Zhu May 12th, 2020 Native exotics order came today with two Akazukin veitchiis
*  Leetcode 502 | hard | med
*  Category: Greedy
*/

using namespace std;
#include <queue>
#include <vector>
#include <algorithm>
#include <utility>

int findMaximizedCapital(int k, int W, vector<int>& profits, vector<int>& capital) {
    int N = profits.size();
    priority_queue<int> pq;
    vector<pair<int, int>> pc; 
    for(int i = 0; i < N; ++i){
        int profit = profits[i]; int cap = capital[i];
        pc.push_back(pair{profit, cap});
    }
    
    sort(begin(pc), end(pc), [](pair<int, int>& p1, pair<int, int>& p2){ return p1.second < p2.second; });
    int ret = W;
    int i = 0;
    
    while(k--){
        for(; i < N; ++i){
            auto [profit, cap] = pc[i];
            if(cap > ret) break;
            pq.push(profit);
        }
        if(pq.size()){
            ret += pq.top(); pq.pop();
        }
    }
    
    return ret;
}