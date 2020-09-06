/* Nathan Zhu Stockton, CA, May 12th, 2020. 6:45 am  Calling Sophie from Amex next week! 
*  Leetcode 1136 | hard | not bad, may be hard for ppl who learned dfs top sort.
*  Category: Topoplogical sort
*/
#include <unordered_map>
#include <vector>
#include <set>

using namespace std;

int minimumSemesters(int N, vector<vector<int>>& relations) {
    unordered_map<int, vector<int>> postreq;
    unordered_map<int, set<int>> prereq;
    if(N == 0) return 0;  // 0 sem for 0 classes
    
    for(auto vec : relations){
        int pre(vec[0]), post(vec[1]);
        postreq[post].push_back(pre);
        prereq[pre].insert(post);
    }
    
    // initial courses we can take
    vector<int> curr;
    for(int i = 1; i <= N; ++i){
        if(!prereq.count(i)) curr.push_back(i);
    }

    int num_taken(0), ret(0);
    while(num_taken != N && curr.size()){
        num_taken += curr.size();
        ret++;
        
        for(auto course: curr){
            for(auto post : postreq[course]){
                prereq[post].erase(course);
            }
        }
        curr.clear();
        
        for(auto& [k, v]: prereq){
            if(v.empty()) curr.push_back(k);
        }
        
        for(auto course: curr) prereq.erase(course);
    }
    
    return (num_taken == N) ? ret : -1;
}