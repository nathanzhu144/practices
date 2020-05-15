/* Nathan Zhu May 8th, 2020 Starting salesforce in a weekish.
*  Leetcode 289 | medium | easy
*  Category: Misc tricks
*/

#include <vector>

using namespace std;
int count_neigh(vector<vector<int>>& board, int r, int c){
    vector<int> dr = {1, 0, -1, 0, 1, -1, -1, 1};
    vector<int> dc = {0, 1, 0, -1, 1, -1, 1, -1};
    int ret = 0;
    
    for(int i = 0; i < 8; ++i){
        int newr = r + dr[i], newc = c + dc[i];
        if(0 <= newr and newr < board.size() and 0 <= newc and newc < board[0].size() and board[newr][newc] & 1){
            ret++;
        }
    }
    return ret;
}

void gameOfLife(vector<vector<int>>& board) {
    if(!board.size() or !board[0].size()) return;
    int R = board.size(), C = board[0].size();
    
    for(int r = 0; r < R; ++r){
        for(int c = 0; c < C; ++c){
            int neigh = count_neigh(board, r, c);
            if(board[r][c] == 1 and (neigh < 2 or neigh > 3)) board[r][c] = 3;
            if(board[r][c] == 0 and (neigh == 3)) board[r][c] = 2;
        }
    }
    
    for(int r = 0; r < R; ++r){
        for(int c = 0; c < C; ++c){
            if(board[r][c] == 2) board[r][c] = 1;
            if(board[r][c] == 3) board[r][c] = 0;
        }
    }
}