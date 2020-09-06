/* Nathan Zhu Snowflake OA, for Fall Co-op June 11th, 2020
*  Leetcode n/a | n/a | medium?
*  Category: Not sure, I did DFS, but timed out.
*
*  Gridland has moves from (0, 0) to (r, c).
*  We can either move (r + 1, c) or (r, c + 1)
*  If we move (r + 1), we add a H for Horizontal
*  If we move (c + 1), we add a V for Vertial
*
*  So a move from (0, 0) to (2, 2) could be HHVV, HVHV, VVHH, etc.
*  We want to find the kth one alphabetically sorted.
*
*  Wasn't sure how to do this one.
*/

#include <string>
#include <vector>
#include <iostream>
#include <sstream>

using namespace std;
int gk = 0;

void dfs(int r, int c, int tr, int tc, string& curr, vector<string>& allstrs){
    if(r > tr || c > tc) return;
    if(gk < 0) return;
    if(r == tr && c == tc){
        if(gk == 0) allstrs.push_back(curr);
        gk--;
        return;
    }

    curr += "H";
    dfs(r + 1, c, tr, tc, curr, allstrs);
    curr.pop_back();
    curr += "V";
    dfs(r, c + 1, tr, tc, curr, allstrs);
    curr.pop_back();
}

vector<string> getSafePaths(vector<string> journeys) {
    vector<string> ret;
    for(auto journey : journeys){
        stringstream s(journey);
        string temp;
        vector<string> items;
        while(getline(s, temp, ' ')){
            items.push_back(temp);
        }

        int x(stoi(items[0])), y(stoi(items[1])), k(stoi(items[2]));
        string curr;
        vector<string> allstrs;
        gk = k;
        dfs(0, 0, x, y, curr, allstrs);
        ret.push_back(allstrs[0]);

    }
    return ret;
}