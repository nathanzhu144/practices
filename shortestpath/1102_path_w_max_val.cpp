/* Nathan Zhu May 8th, 2020
*  Leetcode 1102 | medium | the C++ was harder than the Q lol
*  Category: Djikstra
*
*  For the life of me could not figure out how to put a std::tuple in a pq.
*  Also, what's with pq(comp), why do we pass in the lambda there too?  And what's the point of decltype?
*  Got lots of C++ to learn.
*
*  Also damn structured binding is cool.
*
*/
#include <queue>
#include <vector>
#include <utility>
#include <tuple>
using namespace std;

struct Pos{
    int val;
    int r;
    int c;
};


int maximumMinimumPath(vector<vector<int>>& A) {
    if(!A.size() or !A[0].size()) return -1;
    int R = A.size(), C = A[0].size();
    
    auto comp = [](const Pos& a, const Pos& b){
        return a.val < b.val;
    };
    
    priority_queue<Pos, std::vector<Pos>, decltype(comp)> pq(comp);
    pq.push(Pos{A[0][0], 0, 0});
    
    while(pq.size()){
        auto [maxval, r, c] = pq.top();
        if(r == R - 1 and c == C - 1) return maxval;
        pq.pop();
        //cout << r << " " << c;
        for(auto vec : vector<tuple<int, int>>({{0, 1}, {1, 0}, {-1, 0}, {0, -1}})){
            auto [dr, dc] = vec;
            int newr = r + dr, newc = c + dc;
            if(0 <= newr and newr < R and 0 <= newc and newc < C and A[newr][newc] != -1){
                pq.push(Pos{min(maxval, A[newr][newc]), newr, newc});
                A[newr][newc] = -1;
            }
        }
    }