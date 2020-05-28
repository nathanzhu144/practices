/* Nathan Zhu May 19th, 2020 Second day of work at Salesforce!
*  Leetcode 1351 | easy | think this should be a medium
*  Category: Misc tricks
*  Basically the same idea as leetcode 240. 
*
*  Runtime M + N
*  BE CAREFUL WITH POINTERS, ALWAYS THINK ABOUT WHICH WAY THE POINTERS ARE MOVING.
*  If in doubt, check all r, c conditions before every access.
*/

#include <vector>

using namespace std;
int countNegatives(vector<vector<int>>& grid) {
    if(!grid.size() || !grid[0].size()) return 0;
    int R(grid.size()), C(grid[0].size());
    int r(R - 1), c(0);
    int ret = R * C;
    
    while(r >= 0 && c < C){
        if(c < C && grid[r][c] >= 0){
            ret -= (r + 1);
            c++;
        }
        while(r >= 0 && c < C && grid[r][c] < 0) r--;
    }
    
    return ret;
}