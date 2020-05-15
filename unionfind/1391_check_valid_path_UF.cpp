/*  Nathan Zhu April 13th, 2020. Damn I am tired, nearly 3 am.  Stockton, CA COVID-19
*   Leetcode 1391 | medium | kinda hard for a med
*   Category: union find
*
*   This solution is really smart.  Basically, we multiply the grid by 2, to get a new grid.
*   Then, instead of imagining each item in the grid as a square, we imagine it as a node, with
*   four surrounding nodes.  We do UF on the surrounding 4 nodes, and if two nodes do UF
*   successfully on a node, there is a path through that node.
*
*   TLE on leetcode, but I think this is an ok soln, Lee215's python soln where he 
*   doesn't pass anything around is very slow, and I think it is on the edge.
*/

#include <unordered_map>
#include <string>
#include <vector>

using namespace std;


int transform(int r, int c, int n){
    return r * n + c;
}

int find(unordered_map<int, int>& parent, int curr){
    if(parent[curr] != curr) parent[curr] = find(parent, parent[curr]);
    return parent[curr];
}

void uni(unordered_map<int, int>& parent, int curr1, int curr2){
    int p1(find(parent, curr1)), p2(find(parent, curr2));
    if(p1 == p2) return;
    parent[p1] = p2;
}

bool hasValidPath(vector<vector<int>>& grid) {
    int R(grid.size()), C(grid[0].size());
    unordered_map<int, int> parent;
    int n = 2 * C + 2;
    
    for(int r = 0; r <= (2 * R) + 1; ++r){
        for(int c = 0; c <= (2 * C) + 1; ++c){
            parent[transform(r, c, n)] = transform(r, c, n);
        }
    }
    
    for(int r = 0; r < R; ++r){
        for(int c = 0; c < C; ++c){
            int mrow(2 * r  + 1), mcol(2 * c + 1);
            string type = to_string(grid[r][c]);
            int transformed = transform(mrow, mcol, n);
            vector<string> union_type = {"256", "234", "135", "146"};
            if(union_type[0].find(type) != string::npos) 
                uni(parent, transformed, transform(mrow - 1, mcol, n));  // top of square
            if(union_type[1].find(type) != string::npos) 
                uni(parent, transformed, transform(mrow + 1, mcol, n));  //bottom
            if(union_type[2].find(type) != string::npos) 
                uni(parent, transformed, transform(mrow, mcol - 1, n));  //left
            if(union_type[3].find(type) != string::npos) 
                uni(parent, transformed, transform(mrow, mcol + 1, n));  //right
        }
    }
    return find(parent, transform(1, 1, n)) == find(parent, transform(2 * (R - 1) + 1, 2 * (C - 1) + 1, n));
}