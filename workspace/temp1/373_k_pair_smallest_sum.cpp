/** Nathan Zhu, Stockton, CA.May 28th, 2020, 10:11 pm Saw amber and her mom on a walk today.  They were surprised Renying is working at Facebook.
 *  Leetcode 373 | medium | medium
 *  Category: Priority queue
 *  
 *  Idea is simple, same as the one where we find k-th largest sum in a sorted matix.
 * 
 * 
*/



#include <vector>
#include <string>
#include <queue>
#include <utility>
#include <set>
#include <algorithm>

using namespace std;

vector<vector<int>> kSmallestPairs(vector<int>& nums1, vector<int>& nums2, int k) {
    int N1(nums1.size()), N2(nums2.size());
    if(!N1 or !N2) return {};
    
    typedef pair<int, int> pr;
    auto fx = [&] (auto a, auto b) { 
        auto [a1, a2] = a;
        auto [b1, b2] = b;
        return nums1[a1] + nums2[a2] > nums1[b1] + nums2[b2]; };
    priority_queue<pr, vector<pr>, decltype(fx)> pq(fx);
    vector<vector<int>> ret;
    set<string> visited;
    pq.emplace(0, 0);
    
    while(k && pq.size()){
        auto [i1, i2] = pq.top(); pq.pop();
        string mapping = to_string(i1) + " " + to_string(i2);
        if(visited.count(mapping)) continue;
        visited.insert(mapping);
        
        if(i1 + 1 < N1) pq.emplace(i1 + 1, i2);
        if(i2 + 1 < N2) pq.emplace(i1, i2 + 1);
        
        k--;
        ret.push_back({nums1[i1], nums2[i2]});
    }
    
    return ret;
}