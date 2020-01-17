/**
 * Nathan Zhu Jan 10th, 2020 7:29 pm Foundry Lofts
 * Leetcode 149 | hard | effin hard
 * 
 * There are some nasty edge cases, like what if two points
 * overlap.  
 * 
 * Note we use GCD to store slope.
 */


#include <vector>
#include <unordered_map>
#include <string>

using namespace std;
int gcd(int a, int b){
    return b == 0 ? a : gcd(b, a % b);
}
int maxPoints(vector<vector<int>>& points) {
    int ret = 0;
    int N = points.size();
    
    for(int i = 0; i < N; ++i){
        unordered_map<string, int> table;
        int dup = 1;                                           // this is a counter for overlapping points
        
        for(int j = i + 1; j < N; ++j){
            if(points[i][0] == points[j][0] and points[i][1] == points[j][1])
                dup += 1;
            else{
                int dx = points[i][0] - points[j][0];
                int dy = points[i][1] - points[j][1];
                int g = gcd(dx, dy);
                
                table[to_string(dx / g) + to_string(dy / g)] += 1;
            }
        }
        ret = max(dup, ret);                                    // for cases where this is just like point point
        for(auto& p: table) ret = max(ret, p.second + dup);
    }
    
    return ret;
    
}