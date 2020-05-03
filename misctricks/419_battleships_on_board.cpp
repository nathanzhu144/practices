/*  Nathan Zhu 10:19 pm, April 30th, 2020.  Just finished 376  final exam today.  Whatta beast of an exam.
*   Leetcode 419 | medium | medium
*   Category: Misc tricks
*
*   How to count battleships in O(1) space and in one pass.  Only count leftmost or topmost square
*   of battleship.
*/

#include <vector>
using namespace std;

int countBattleships(vector<vector<char>>& board) {
    if(!board.size()) return 0;
    
    int R = board.size(), C = board[0].size();
    int ret = 0;
    
    for(int r = 0; r < R; ++r){
        for(int c = 0; c < C; ++c){
            if(board[r][c] == 'X' and (r == 0 or board[r - 1][c] == '.') and (c == 0 or board[r][c - 1] == '.')) ret++;
        }
    }
    
    return ret;
}